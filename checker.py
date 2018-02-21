import imp
import os
import yaml
import traceback
import sys

if sys.version_info.major != 3:
    import subprocess
    try:
        subprocess.call(['/usr/bin/env', 'python3'] + sys.argv)
    except:
        print >>sys.stderr, "must be run with python 3"
    finally:
        sys.exit(1)

problem_dir = os.path.dirname(os.path.realpath(__file__))
problem_names = os.listdir(problem_dir)

valid = []
invalid = dict()

required_filenames = ["problem.yml", "description.md", "grader.py"]
required_keys = ["author", "value", "title", "category"]


def tableprint(rows):
    # https://stackoverflow.com/a/5910078
    if len(rows) > 1:
        headers = ["path", "title", "category", "author", "value", "solution", "hint"]
        lens = dict()
        for key in headers:
            lens.update({
                key: len(max([x.get(key, "") for x in rows] +
                             [key], key=lambda x: len(str(x))))
            })
        formats = []
        hformats = []
        for key in headers:
            if isinstance(rows[0].get(key, ""), int):
                formats.append("%%%dd" % lens[key])
            else:
                formats.append("%%-%ds" % lens[key])
            hformats.append("%%-%ds" % lens[key])
        pattern = " | ".join(formats)
        hpattern = " | ".join(hformats)
        separator = "-+-".join(["-" * lens[key] for key in headers])
        print(hpattern % tuple(headers))
        print(separator)

        for line in rows:
            print(pattern % tuple(line.get(key, "") for key in headers))
    elif len(rows) == 1:
        row = rows[0]
        hwidth = len(max(row.keys(), key=lambda x: len(x)))
        for i in range(len(row)):
            print("%*s = %s" % (hwidth, row.keys()[i], row[i]))


def check_problem(name):
    folder = os.path.join(problem_dir, name)
    errors = []
    missing = []
    problem = dict(path=name)
    grader = None
    for name in required_filenames:
        fullname = os.path.join(folder, name)
        if not os.path.exists(fullname):
            missing.append(name)
            errors.append("could not locate '{}'".format(name))
    metadata = None
    if "problem.yml" not in missing:
        metadata = yaml.load(open(os.path.join(folder, "problem.yml")))
        missing_keys = list()
        for key in required_keys:
            if metadata.get(key) is None:
                missing_keys.append(key)
                errors.append("missing key from problem.yml: '{}'".format(key))
        try:
            if metadata.get("threshold") and int(metadata.get("threshold")) > 0:
                assert metadata.get("weightmap"), "Missing weightmap"
        except Exception as e:
            errors.append("weightmap/threshold failure: {}".format(str(e)))
        if not metadata.get("hint"):
            problem.update(dict(hint="x"))
        if not missing_keys:
            problem.update(dict(
                author=metadata.get("author"),
                category=metadata.get("category"),
                title=metadata.get("title"),
                value=metadata.get("value"),
            ))
            if metadata.get("autogen") == True:
                # need generate function
                pass
        if "grader.py" not in missing:
            grader = imp.new_module("grader")
            curr = os.getcwd()
            os.chdir(folder)
            with open(os.path.join(folder, "grader.py")) as f:
                data = f.read()
            programming = metadata.get("programming")
            if not programming:
                try:
                    exec(data, grader.__dict__)
                except Exception as e:
                    errors.append("grader has a syntax error: '{}'".format(e))
                else:
                    if not hasattr(grader, "grade"):
                        errors.append("grader is missing 'grade' function")
            os.chdir(curr)

    problem.update(dict(solution="+" if os.path.exists(os.path.join(folder, "solution.txt")) else ""))
    return problem, errors


if __name__ == "__main__":
    import sys
    sort_by = sys.argv[1] if len(sys.argv) > 1 else "value"

    for name in problem_names:
        if name.startswith("."):
            continue
        problem_folder = os.path.join(problem_dir, name)
        if not os.path.isdir(problem_folder):
            continue
        try:
            problem, errors = check_problem(name)
            if not errors:
                valid.append(problem)
            else:
                invalid[name] = errors
        except:
            invalid[name] = [
                "error when trying to check problem", traceback.format_exc()]
    valid.sort(key=lambda p: p.get(sort_by, 0))

    # report

    print("[ Report ]")
    print()
    print("valid problems ({}):".format(len(valid)))
    tableprint(valid)
    print()
    print("invalid problems ({}):".format(len(invalid.items())))
    for name, errors in invalid.items():
        print(" - {}".format(name))
        for error in errors:
            print("    * {}".format(error))
