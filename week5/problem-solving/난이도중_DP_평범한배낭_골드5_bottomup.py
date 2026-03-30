# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

def print_table(dp):
    for row in dp[1:]:
        print(* row[1:])


n, k = map(int, input().split())

items = [None]
for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

dp = [0] * (k + 1)

for i in range(1, n + 1):
    wi, vi = items[i]
    for j in reversed(range(wi, k + 1)):
        dp[j] = max(dp[j], dp[j - wi] + vi)

print(dp[k])






