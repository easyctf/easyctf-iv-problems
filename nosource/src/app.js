const express = require('express');
const crypto = require('crypto');
const path = require('path');
const logger = require('morgan');
const session = require('express-session');
const mustacheExpress = require('mustache-express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const helmet = require('helmet');
const useragent = require('express-useragent');
const MemoryStore = require('memorystore')(session);


function generateToken() {
  return crypto.randomBytes(32).toString('base64');
}

function processToken(input, init, soupify) {
  const token = Buffer.from(input, 'base64');
  if (token.length != 32) {
    console.error("invalid token from input: " + input);
    return '';
  }

  if (soupify) {
    token.write('soupd', 32 - 5, 5, 'binary');
  }

  let k = init & 0xff;
  for (let i = 0; i < token.length; i++) {
    k ^= token[i];
    token[i] = k;
  }
  return token.toString('base64');
}

const app = express();
app.engine('mustache', mustacheExpress());
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'mustache');

var sess = {
  name: 'sid',
  secret: "i am a cat who goes mrrroowww",
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,
  },
  store: new MemoryStore({
    checkPeriod: 1000 * 60 * 60  // prune expired entries
  }),
};

var helmetConfig = {
  dnsPrefetchControl: false,
};

if (app.get('env') === 'production') {
  app.set('trust proxy', 1);
  sess.cookie.secure = true;
}

app.use(logger('dev'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(cookieParser());
app.use(session(sess));
app.use(helmet(helmetConfig));
app.use(useragent.express());


// img and css can be cached
app.use('/static/css', express.static(
  path.join(__dirname, 'public', 'css'),
  { lastModified: false }));

app.use('/static/img', express.static(
  path.join(__dirname, 'public', 'img'),
  { lastModified: false }));


// nothing else should be cached
app.use(function (req, res, next) {
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate');
  res.setHeader('Pragma', 'no-cache');
  next();
});

// handle js files
const static_js_options = {
  root: path.join(__dirname, 'public', 'js'),
  cacheControl: false,
  lastModified: false,
  etag: false,
};

app.get('/static/js/bootstrap.min.js', function (req, res, next) {
  if (req.session.token && req.session.tokenTime) {
    console.log('serving modified bootstrap.min.js');
    res.sendFile('mod-bootstrap.min.js', static_js_options);
    return;
  }
  next();
});

app.get('/static/js/popper.min.js', function (req, res, next) {
  if (req.session.successOnce) {
    delete req.session.successOnce;
    console.log('serving modified popper.min.js');
    res.sendFile('mod-popper.min.js', static_js_options);
    return;
  }
  next();
});

app.use('/static/js', express.static(
  static_js_options.root, static_js_options));


// do not filter these by user agent
app.get('/', function (req, res) {
  delete req.session.tokenTime;
  const token = generateToken();
  req.session.token = token;
  res.render('index', { token: token });
});

app.get('/soupd', function (req, res) {
  req.session.destroy();
  if (req.cookies.token) {
    res.clearCookie('token');
  }
  res.render('soupd');
});

app.get('/useragent', function (req, res) {
  res.send(req.useragent);
});

// nosource junior!!
app.get('/jr/', function (req, res) {
  res.render('jr', {noSourceJr: true});
});

app.get('/www.google-analytics.com/analytics.js', function (req, res) {
  res.sendFile('fake-analytics.js', static_js_options);
});

// filter everything below by user agent
app.use(function (req, res, next) {
  if (!req.useragent.isChrome) {
    res.redirect('/soupd?7');
  } else {
    next();
  }
});

app.post('/login', function (req, res) {
  if (req.session.token) {
    const goodToken = processToken(req.session.token, 0x20, false);
    const receivedToken = req.body.token;
    console.log('receivedToken:', receivedToken);
    console.log('goodToken    :', goodToken);
    req.session.token = '';

    if (receivedToken === goodToken) {
      // generate another token, with time
      const token = generateToken();
      req.session.token = token;
      req.session.tokenTime = new Date();

      res.setHeader('Refresh', '2; url=/soupd?4');
      res.render('test', {
        token: token,
        timeoutSoupd: true,
      });
      return;
    }
  }
  res.redirect('/soupd?5');
});

app.get('/login', function (req, res) {
  //console.log("req.session: " + JSON.stringify(req.session));
  //console.log("req.cookies: " + JSON.stringify(req.cookies));

  if (req.cookies.token && req.session.token && req.session.tokenTime) {
    const duration = new Date() - new Date(req.session.tokenTime);
    const soupToken = processToken(req.session.token, 20, true);
    //const nosoupToken = processToken(req.session.token, 20, false);
    const receivedToken = req.cookies.token;

    console.log('receivedToken:', receivedToken);
    console.log('soupToken    :', soupToken);
    //console.log('nosoupToken  :', nosoupToken);
    console.log('duration', duration);

    delete req.session.token;
    delete req.session.tokenTime;
    res.clearCookie('token');

    if (receivedToken === soupToken) {
      if (duration < 5000) {
        req.session.successOnce = true;
        res.render('success', { timeoutSoupd: true });
        return;
      }
      res.redirect('/soupd?8');
      return;
    }
    res.redirect('/soupd?9');
    return;
  }
  res.redirect('/soupd?6');
});

module.exports = app;

