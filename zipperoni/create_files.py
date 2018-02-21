#!/usr/bin/env python3

import binascii
import random
import hashlib
import os
import string
import subprocess

def write_zip(fname, pwd, files):
    rc = subprocess.call(['7z', 'a', '-p' + pwd, '-y', fname] + files)
    if rc != 0:
        print('Return code :(', rc)

def generate_filename(size):
    b = bytes(random.getrandbits(8) for _ in range(size))
    return binascii.hexlify(b).decode()

def generate_pattern(size, n):
    if n < 4:
        choices = '0_'
    else:
        choices = '0aA_'
    lst = [random.choice(choices) for _ in range(size)]
    return ''.join(lst)

def generate_password(pattern):
    out = []
    for c in pattern:
        choices = ''
        if c == '0':
            choices = string.digits
        elif c == 'a':
            choices = string.ascii_lowercase
        elif c == 'A':
            choices = string.ascii_uppercase
        elif c == '_':
            choices = '_'
        out.append(random.choice(choices))
    return ''.join(out)


random.seed(195402)

base = 'zip_files/'
os.makedirs(base, exist_ok=True)

fname = os.path.join(base, 'begin.zip')
pwd = 'coolkarni'

for i in range(25):
    next_fname = os.path.join(base, generate_filename(6) + '.zip')
    next_pattern = generate_pattern(6, i)
    next_pwd = generate_password(next_pattern)
    next_pwd_hash = hashlib.sha1(next_pwd.encode()).hexdigest()

    print('writing to', fname)
    print('things:', next_fname, next_pattern, next_pwd)

    with open('filename.txt', 'w') as f:
        f.write(next_fname + '\n')
    with open('pattern.txt', 'w') as f:
        f.write(next_pattern + '\n')
    with open('hash.txt', 'w') as f:
        f.write(next_pwd_hash + '\n')
    write_zip(fname, pwd, ['filename.txt', 'pattern.txt', 'hash.txt'])

    fname = next_fname
    pwd = next_pwd




# final zip contains flag
print('writing to', fname)
print('(writing flag)')

write_zip(fname, pwd, ['flag.txt'])


# generate trash files
for i in range(74):
    fname = os.path.join(base, generate_filename(6) + '.zip')

    next_fname = os.path.join(base, generate_filename(6) + '.zip')
    next_pattern = generate_pattern(6, i)
    next_pwd = generate_password(next_pattern)
    next_pwd_hash = hashlib.sha1(next_pwd.encode()).hexdigest()

    print('writing to', fname)
    print('things:', next_fname, next_pattern, next_pwd)

    with open('filename.txt', 'w') as f:
        f.write(next_fname + '\n')
    with open('pattern.txt', 'w') as f:
        f.write(next_pattern + '\n')
    with open('hash.txt', 'w') as f:
        f.write(next_pwd_hash + '\n')
    write_zip(fname, pwd, ['filename.txt', 'pattern.txt', 'hash.txt'])

# output file
subprocess.call(['tar', 'cvf', 'zip_files.tar', 'zip_files/'])
subprocess.call(['rm', '-rf', 'zip_files/'])

# cleanup
os.remove('filename.txt')
os.remove('pattern.txt')
os.remove('hash.txt')

