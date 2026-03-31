# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
sys.setrecursionlimit(10**5)

def solve(index, m):
    if index < 0:
        return 0
    if index == 0:
        return 1 if m % coins[index] == 0 else 0
    if m == 0:
        return 1
    if m < 0:
        return 0
    if dp[index][m] != -1:
        return dp[index][m]

    dp[index][m] = solve(index - 1, m) + solve(index, m - coins[index])

    return dp[index][m]


tc = int(input())

for _ in range(tc):
    coin_count = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    # dp = [[-1] * (len(coins) + 1) for _ in range(m + 1)]
    dp = [[-1] * (m + 1) for _ in range(len(coins))]

    print(solve(len(coins) - 1, m))




