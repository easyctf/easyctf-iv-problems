const express = require('express');
const logger = require('morgan');
const mustacheExpress = require('mustache-express');
const multer = require('multer');
const helmet = require('helmet');

const child_process = require('child_process');
const fs = require('fs');
const rimraf = require('rimraf');
const path = require('path');


// constants

const SESSION_KEY = 'moo moo i am a cat that goes moo';
const MAX_IMAGE_SIZE = 1000000;  // 1 mb
const PROCESS_TIMEOUT = 30000;  // 30 s

const UPLOAD_DIR = path.join(__dirname, '/uploads');
const STATIC_DIR = path.join(__dirname, '/public');
const TEMPLATES_DIR = path.join(__dirname, '/views');
const ASCII_SCRIPT = path.join(__dirname, '/run.py');


// app config

const app = express();
app.engine('mustache', mustacheExpress());
app.set('views', TEMPLATES_DIR);
app.set('view engine', 'mustache');

var upload = multer({
  dest: UPLOAD_DIR,
  limits: {
    fileSize: MAX_IMAGE_SIZE,
  },
});

var helmetConfig = {
  dnsPrefetchControl: false,
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
    },
  },
};

if (app.get('env') === 'production') {
  app.set('trust proxy', 1);
}

app.use(logger('dev'));
app.use(helmet(helmetConfig));
app.use('/static', express.static(STATIC_DIR));


// routes

app.get('/', function (req, res) {
  res.render('index');
});

app.post('/', upload.single('image'), function (req, res) {
  var filename = req.file.filename;
  console.log('uploaded ' + req.file.originalName + ' to ' + filename);

  var folder = fs.mkdtempSync(path.join(UPLOAD_DIR, 'temp-'));
  fs.renameSync(path.join(UPLOAD_DIR, filename), path.join(folder, 'image'));
  fs.copyFileSync(ASCII_SCRIPT, path.join(folder, 'run.py'));
  console.log('temporary folder ' + folder);

  // start process
  var child = child_process.execFile(
    'nsjail', [
      '--quiet', '--config', 'pixelly.cfg', '--',
      '/usr/bin/python3', 'run.py', 'image'
    ],
    {
      timeout: PROCESS_TIMEOUT,
      env: { 'HOME': folder },
    },
    function (err, stdout, stderr) {
      if (err) {
        console.error('app.js: process error: ' + err);
      }
      var output = stdout + '\n' + stderr;
      res.render('display', { content: output });
    });

  console.log('app.js: spawned process for filename', filename);

  child.on('exit', function (code, signal) {
    if (code != 0) {
      console.error('app.js: process exited with ' +
        'code ' + code + ', signal ' + signal );
    }
    rimraf(folder, function (err) {
      if (err) {
        console.error('app.js: error during unlink: ' + err);
      }
    });
  });

});

app.use(function (err, req, res, next) {
  console.error(err.stack);
  res.status(500);
  res.render('display', { content: err.stack });
});

module.exports = app;

