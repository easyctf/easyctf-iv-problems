n = 26 - int(input())

alp = list('abcdefghijklmnopqrstuvwxyz')

def shift(s, b):
    o = ''
    for i in s:
        if i in alp:
            i = alp[(alp.index(i) + b) % 26]
        o += i
    return o

print(shift(input(), n))