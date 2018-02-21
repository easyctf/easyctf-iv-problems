#!/usr/bin/env python3

import random
import string

def generate_flag(seed):
    r = random.Random()
    r.seed(seed ^ 0x1337)
    s = ''.join(r.choice(string.hexdigits) for i in range(16))
    return 'hello_there!_' + s

seed = None
while True:
    try:
        seed = int(input("enter your player key: "))
        break
    except ValueError:
        print("please enter a valid number!")

flag = generate_flag(seed)
print("thanks! here's your key: easyctf{%s}" % flag)
