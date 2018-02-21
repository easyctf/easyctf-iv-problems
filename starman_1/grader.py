import sys
sys.setrecursionlimit(5000)


N, W = map(int, input().split())

dat = [list(map(int, input().split())) for i in range(N)]

memo = [[-1] * (W + 1) for i in range(N)]

# https://en.wikipedia.org/wiki/Knapsack_problem

def ans(ind, wr):
    if ind == N:
        return 0
    if memo[ind][wr] != -1:
        return memo[ind][wr]
    best = ans(ind + 1, wr)
    if dat[ind][1] <= wr:
        best = max(best, dat[ind][0] + ans(ind + 1, wr - dat[ind][1]))
    memo[ind][wr] = best
    return best
    
print(ans(0, W))
