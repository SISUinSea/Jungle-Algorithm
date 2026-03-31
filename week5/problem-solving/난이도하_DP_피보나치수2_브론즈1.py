# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())

dp = [0] * max(n + 1, 2 + 1)
dp[1] = dp[2] = 1
if n >= 3:
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i - 2]

print(dp[n])