import math
from Crypto.PublicKey import RSA
import binascii
import os
from io import StringIO
import binascii

import random as rdom

_mrpt_num_trials = 5


def gen_flag(random):
    return "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(18)])


def generate_c(random):
    flag = "easyctf{" + gen_flag(random) + "}"
    M = int(binascii.hexlify(bytes(flag, "utf-8")), 16)

    key = RSA.generate(2048)
    n = key.n
    e = key.e
    p = key.p
    q = key.q

    phi = (p-1)*(q-1)
    d = key.d

    leak = 2*d+phi

    c = pow(M, e, n)
    txt = "n={}\ne={}\nc={}\n2d+phi(n)={}".format(n, e, c, leak)
    # txt = 'n='+str(n)+'\ne= 65537\nc='+str(c)+'\n2d+phi(n)='+leak
    return StringIO(txt)


def generate(random):
    return dict(files={
        "hiddenkey.txt": generate_c(random)
    })


def grade(random, key):
    flag = gen_flag(random)
    if key.find(flag) >= 0:
        return True, "Correct!"
    return False, "Nope."
