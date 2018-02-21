#!/usr/bin/env python2

# thanks python 2
from __future__ import print_function
import io
open = io.open

# other imports
from pwn import *
import csv
import re

QUESTION_CHOICES = dict([
        ('land area (m^2)', 'ALAND'),
        ('water area (m^2)', 'AWATER'),
        ('latitude (degrees)', 'INTPTLAT'),
        ('longitude (degrees)', 'INTPTLONG'),
])


def read_data():
    with open('Gaz_zcta_national.txt', newline='') as csvfile:
        lines = [line.rstrip() for line in csvfile.readlines()]

    data = {}
    reader = csv.DictReader(lines,
            dialect=csv.excel_tab,
            skipinitialspace=True)
    for row in reader:
        data[row['GEOID']] = row

    return data


def main():
    data = read_data()

    conn = remote('c1.easyctf.com', 12483)
    #conn = process(['./server.py'])

    print('Waiting for intro...')
    print(conn.recvuntil('Go!', timeout=5))

    for t in range(50):
        inp = conn.recvuntil('? ')
        print('Read:', repr(inp))
        m = re.search(r'What is the (.*) of the zip code ([0-9]*)\?', inp)
        c = m.group(1)
        z = m.group(2)
        ans = data[z][QUESTION_CHOICES[c]]
        print('Parsed: question {}, zipcode {}, answer {}'
                .format(c, z, ans))
        conn.sendline(ans)

    conn.interactive()

if __name__ == '__main__':
    main()
