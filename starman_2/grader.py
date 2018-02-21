import functools, math
N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    
def rt(a, b, c):
    ba = (b[0] - a[0], b[1] - a[1])
    ca = (c[0] - a[0], c[1] - a[1])
    return ba[0] * ca[1] - ba[1] * ca[0] > 0

def srt(a, b):
    return a[0] - b[0] if a[1] == b[1] else a[1] - b[1]

def dist(l1, l2, p):
    line = (l2[0] - l1[0], l2[1] - l1[1])
    l = line[0] * line[0] + line[1] * line[1]
    t = (p[0] - l1[0], p[1] - l1[1])
    t = t[0] * line[0] + t[1] * line[1]
    t /= l
    ans = (line[0] * t, line[1] * t)
    ans = (ans[0] + l1[0], ans[1] + l1[1])
    ans = (ans[0] - p[0], ans[1] - p[1])
    return math.sqrt(ans[0] * ans[0] + ans[1] * ans[1])

def cvh(pts):
    s = list(sorted(pts, key=functools.cmp_to_key(srt)))
    n, j, k = len(s), 2, 2
    if n < 3:
        return s
    
    lo, up = [None] * n, [None] * n
    lo[0] = s[0]
    lo[1] = s[1]
    for i in range(2, n):
        p = s[i]
        while j > 1 and not rt(lo[j - 2], lo[j - 1], p):
            j -= 1
        lo[j] = p
        j += 1

    up[0] = s[-1]
    up[1] = s[-2]
    for i in range(n - 3, -1, -1):
        p = s[i]
        while k > 1 and not rt(up[k - 2], up[k - 1], p):
            k -= 1
        up[k] = p
        k += 1
        
    res = []
    for i in range(k):
        res.append(up[i])
    for i in range(1, j - 1):
        res.append(lo[i])
    
    return res


ch = cvh(points)
#print(ch)
#print("here")

if len(ch) < 3:
    print(0)
    exit(0)
    
N = len(ch)
o = 0
mn = 10 ** 18
for i in range(N):
    a, b = ch[i], ch[(i + 1) % N]
    #print("seg: %s %s\n" % (a, b))
    while dist(a, b, ch[o]) <= dist(a, b, ch[(o + 1) % N]):
#        print(a, b, ch[o], dist(a, b, ch[o]))
        o += 1
        o %= N
    mn = min(mn, dist(a, b, ch[o]))
    #print(mn)

print("%.6f" % (mn))