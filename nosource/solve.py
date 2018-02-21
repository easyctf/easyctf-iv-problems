#!/usr/bin/env python
from __future__ import print_function

import re
import json
import requests
from base64 import b64encode, b64decode
from bs4 import BeautifulSoup

HOST = 'http://localhost:3000'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

def process_token(inp, init, soupify):
    token = bytearray(b64decode(inp))
    assert len(token) == 32

    if soupify:
        token[32-5:] = b'soupd'

    k = init & 0xff
    for i in range(len(token)):
        k ^= token[i]
        token[i] = k
    return b64encode(token).decode()


def repeated_xor(a, b):
    length = max(len(a), len(b))
    out = bytearray()
    for i in range(length):
        ca = a[i % len(a)]
        cb = b[i % len(b)]
        out.append(ca ^ cb)
    return out.decode()


def main():
    jar = requests.cookies.RequestsCookieJar()

    # first, extract token0
    r = requests.get(HOST + '/')
    jar.update(r.cookies)
    s = BeautifulSoup(r.text, 'html.parser')
    token0 = s.find(id='token')['value']
    print('token0', token0)

    # now process
    token0 = process_token(token0, 0x20, False)
    print('  >>> ', token0)

    # now extract token1
    r = requests.post(HOST + '/login',
            cookies=jar,
            data={'token': token0},
            headers={'User-Agent': USER_AGENT})
    jar.update(r.cookies)
    s = BeautifulSoup(r.text, 'html.parser')
    token1 = s.find(id='token')['value']
    print('token1', token1)

    # now process
    token1 = process_token(token1, 20, True)
    print('  >>> ', token1)

    # now get source!!
    jar.set('token', token1)
    r = requests.get(HOST + '/login',
            cookies=jar,
            headers={'User-Agent': USER_AGENT})

    # find flag
    m = re.search(r"var f \= '(.*)';", r.text)
    encoded_flag = m.group(1)
    print('encoded_flag', encoded_flag)

    # decode flag with key
    flag = repeated_xor(b64decode(encoded_flag), b'hoo_hoo!')
    print('flag', flag)


if __name__ == '__main__':
    main()

