from itertools import combinations as comb

n, s = map(int, input().split())
nums = [int(u) for u in input().split()]

t = 0
for i in range(1, len(nums) + 1):
    for c in comb(nums, i):
        if sum(c) == s:
            t += 1

print(t)