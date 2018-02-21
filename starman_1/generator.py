from random import randint as ri
c = int(input())

def gc(n,w,mri,mwi):
    o = "{} {}\n".format(n, w)
    for i in range(n):
        o += "{} {}\n".format(ri(1,mri), ri(1,mwi))
    return o.strip()

if c == 1:
    print(gc(5, 15, 15, 15))
elif c == 2:
    print(gc(10, 100, 25, 25))
elif c == 3:
    print(gc(20, 200, 25, 25))
elif c <= 5:
    print(gc(50, 500, 50, 50))
elif c <= 10:
    N = ri(100, 500)
    W = ri(100, 500)
    print(gc(N, W, 10000, ri(int(3 * W / 5), int(5 * W))))
else:
    N = ri(1000, 2000)
    W = ri(1000, 2000)
    print(gc(N, W, 10000, ri(int(3 * W / 5), int(5 * W))))
