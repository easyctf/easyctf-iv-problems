from random import randint as ri
c = int(input())

def gc(n,mx):
    o = "{}\n".format(n)
    for i in range(n):
        o += "{} {}\n".format(ri(0,2*mx)-mx, ri(0,2*mx)-mx)
    return o.strip()

if c == 1:
    print(gc(5, 10))
elif c == 2:
    print(gc(10, 100))
elif c == 3:
    print(gc(20, 10000))
elif c <= 5:
    print(gc(50, 10000))
elif c <= 8:
    N = ri(100, 1000)
    print(gc(N, 10000))
elif c <= 12:
    N = ri(10000, 100000)
    print(gc(N, 10000))
elif c <= 15:
    N = ri(100000, 200000)
    print(gc(N, 10000000))
else:
    print(gc(200000, 100000000))