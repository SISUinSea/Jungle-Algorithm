# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
sys.setrecursionlimit(10**5)

def solve(m, index):
    if dp[index][m] != -1:
        return dp[index][m]
    dp[index][m] = 0
    for i, coin in enumerate(coins[:index + 1]):
        if m - coin < 0: continue
        if m - coin == 0:
            dp[index][m] += 1
        else:
            dp[index][m] += solve(m - coin, i)
    return dp[index][m]


tc = int(input())

for _ in range(tc):
    coin_count = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    # dp = [[-1] * (len(coins) + 1) for _ in range(m + 1)]
    dp = [[-1] * (m + 1) for _ in range(len(coins) + 1)]
    for i in range(1, m + 1):
        if i % coins[0] == 0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    print(solve(m, len(coins)))




