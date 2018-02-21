#!/usr/bin/env python2

# warning: this script takes like 10 minutes to run
# be prepared for it to take a while
# also: sudo apt-get install libgmp-dev libmpc-dev
#       pip install gmpy2

# thanks py2
from __future__ import print_function

import binascii
import datetime
import gmpy2

with open('new_n.txt') as f:
    n = int(f.read())
with open('new_e.txt') as f:
    e = int(f.read())
with open('new_c.txt') as f:
    c = int(f.read())

# calculate p, q
p = gmpy2.isqrt(n)
q = p + 2

# calculate d
totn = (p-1) * (q-1)
d = gmpy2.invert(e, totn)

# calculate dp, dq, qinv
dp = d % (p-1)
dq = d % (q-1)
qinv = gmpy2.invert(p, q)

# decryption! takes a long time
print(1, datetime.datetime.now())
m1 = gmpy2.powmod(c, dp, p)
print(2, datetime.datetime.now())
m2 = gmpy2.powmod(c, dq, q)
print(3, datetime.datetime.now())
h = (qinv * (m1 - m2)) % p
print(4, datetime.datetime.now())
m = m2 + h * q

# decode it (why in binary who knows)
x = str(m)
x = '0' * (-len(x) % 8) + x
x = hex(int(x, 2)).lstrip('0x').rstrip('L')
x = '0' * (-len(x) % 2) + x
print(binascii.unhexlify(x))
