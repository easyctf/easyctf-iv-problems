#!/usr/bin/env python3

import time
flag = "easyctf{ez_t1m1ng_4ttack!}"
def check(s):
    for c in range(min(len(s), len(flag))):
        if c < 3 and flag[c] == s[c]:
            time.sleep(1)
        if flag[c] == s[c]:
            time.sleep(0.3)
        else:
            print("no")
            return
    if len(s) != len(flag):
        print("no")
        return
    print("wowie u got it")
    return

a = input("enter the flag: ")
check(a)
