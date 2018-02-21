primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
          107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227]
import math
import binascii
import os
from io import StringIO
import binascii

import random as rdom

_mrpt_num_trials = 5


def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = rdom.randrange(2, n)
        if try_composite(a):
            return False

    return True  # no base tested showed n as composite


def genBadPrime(k, a, n=39):
    M = 1
    for i in range(n):
        M *= primes[i]
    return k*M + pow(65537, a, M)


def gen_flag(random):
    return "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(18)])


def generate_c(random):
    flag = "easyctf{" + gen_flag(random) + "}"
    p = 4
    q = 4
    while not is_probable_prime(p):
        k1 = random.randint(69000000000, 130000000000)
        a1 = random.randint(2400000000000000, 4600000000000000)
        p = genBadPrime(k1, a1)
    while not is_probable_prime(q):
        k2 = random.randint(69000000000, 130000000000)
        a2 = random.randint(2400000000000000, 4600000000000000)
        q = genBadPrime(k2, a2)
    e = 65537
    n = p * q
    c = pow(int(binascii.hexlify(str.encode(flag)), 16), e, n)
    txt = 'n: '+str(n)+'\ne: 65537\nc: '+str(c)
    return StringIO(txt)


def generate(random):
    return dict(files={
        "hardrsa.txt": generate_c(random)
    })


def grade(random, key):
    flag = gen_flag(random)
    if key.find(flag) >= 0:
        return True, "Correct!"
    return False, "Nope."
