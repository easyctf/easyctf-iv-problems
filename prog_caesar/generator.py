from random import randint as ri
from random import choice as rc
c = int(input())

alp = list('abcdefghijklmnopqrstuvwxyz')
sts = ["i love easyctf", "mikel pls", "aaaaaaaaaaaaaaaaaa", "abcdefghijklmnopqrstuvwxyz", "michael", "summer camp", "a longer string with plenty of words and phrases", "what would an edge case even look like for this problem lol"]

def shift(s, b):
    o = ''
    for i in s:
        if i in alp:
            i = alp[(alp.index(i) + b) % 26]
        o += i
    return o
    
def gc(s, n):
    return "{}\n{}\n".format(n, shift(s, n))

if c == 1:
    print(gc(sts[0], 1))
elif c == 2:
    print(gc(sts[1], 2))
elif c == 3:
    print(gc(sts[2], 3))
else:
    print(gc(rc(sts), c))