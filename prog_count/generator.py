from random import randint as ri
from random import seed as ss
c = int(input())

def gc(n, s, lo, hi):
    o = "{} {}\n".format(n, s)
    o += ' '.join(str(ri(lo,hi)) for i in range(n))
    return o
    
if c == 1:
    print(gc(1, 7, 7, 7))
elif c == 2:
    print(gc(6, 3, -3, 3))
elif c <= 4:
    print(gc(20, 0, -1, 1))
elif c <= 6:
    print(gc(10, 10, 0, 10))
elif c <= 10:
    print(gc(20, ri(-50, 50), -100, -100))
elif c <= 12:
    n, s = ri(10, 20), ri(20, 30)
    print(gc(n, s, -15, 15))
elif c <= 15:
    n, s = 20, ri(-50, 50)
    print(gc(n, s, -50, 50))
else:
    n, s = 20, ri(-10, 10)
    print(gc(n, s, -10, 10))