#!/usr/bin/env python3

import random
import string
import sys

PASSWORD = bytes("egg{going_the_EXTRA_mile!}", "utf-8")
m = 2**31 - 1


def generate_flag(seed):
    r = random.Random()
    r.seed(1337)
    r.seed(seed ^ r.randint(1, m))
    s = "".join(r.choice(string.hexdigits) for i in range(9))
    return "is_anything_safe?_" + s


def decode_key(client_key):
    seed = 0
    barray = []
    for i in range(4):
        b = (client_key[i] ^ PASSWORD[i])
        # print("b=", b)
        seed |= b << (8 * i)
        barray.append(b)
    # print(barray)
    # print(len(client_key))
    if len(client_key) != len(PASSWORD):
        return 0, "Your key is invalid! (0)"
    for i, c in enumerate(PASSWORD):
        # print("client key: {}, barray: {}, c: {}".format(client_key[i], barray[i % 4], c))
        if client_key[i] ^ barray[i % 4] != c:
            return 0, "Your key is invalid! (1)"
    # print("seed =", seed)
    return seed, ""


sys.stdout.write("Enter your key: ")
sys.stdout.flush()
client_key = sys.stdin.buffer.readline()
if client_key[-1] == ord("\n"):
    client_key = client_key[:-1]
seed, error = decode_key(client_key)
if not seed:
    print(error)
    sys.stdout.flush()
    sys.exit(0)
print("the flag is: easyctf{{{}}}".format(generate_flag(seed)))
sys.stdout.flush()
sys.exit(0)
