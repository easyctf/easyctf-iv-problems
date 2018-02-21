from io import StringIO

template = """
<!doctype html>
<html>
    <head>
        <style>
            body {{ font-family: sans-serif; padding-left: 30px; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <h1>Welcome to EasyCTF!</h1>

        <p>The flag is just below:</p>
        <!-- {flag} -->
    </body>
</html>
"""

flag = "hidden_from_the_masses"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def get_problem(random):
    salt = "".join([random.choice("0123456789abcdef") for i in range(6)])
    return salt


def generate(random):
    salt = get_problem(random)
    contents = template.format(flag=("easyctf{%s}" % "{}_{}".format(flag, salt)))
    return dict(files={
        "index.html": StringIO(contents)
    })


def grade(random, key):
    salt = get_problem(random)
    if(key.find("{}_{}".format(flag, salt)) != -1):
        return True, "Good job!"
    return False, "Try again."
