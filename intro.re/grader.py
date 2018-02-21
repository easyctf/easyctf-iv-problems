from io import StringIO
import string

template = """#!/usr/bin/env python3
import binascii
key = "{enckey}"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))
"""

flag_prefix = "char_by_char"


def get_problem(random):
    enckey = "".join([random.choice(string.ascii_letters) for i in range(8)])
    salt = "".join([random.choice(string.hexdigits) for i in range(6)])
    fmtflag = "{}_{}".format(flag_prefix, salt)
    return enckey, fmtflag


def generate(random):
    enckey, fmtflag = get_problem(random)
    contents = template.format(enckey=enckey)
    v = dict()
    exec(contents, v, v)
    enc = v["mystery"]("easyctf{%s}" % fmtflag).decode("utf-8")
    return dict(files={
        "mystery.py": StringIO(contents)
    }, variables={
        "enc": enc
    })


def grade(random, key):
    enckey, fmtflag = get_problem(random)
    if(key.find(fmtflag) != -1):
        return True, "Good job!"
    return False, "Try again."
