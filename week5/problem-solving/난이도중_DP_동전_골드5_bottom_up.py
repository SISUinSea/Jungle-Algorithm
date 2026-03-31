# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

def print_table(dp):
    for row in dp:
        print(*row)

tc = int(input())

for _ in range(tc):
    coin_count = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    # dp = [[-1] * (len(coins) + 1) for _ in range(m + 1)]
    dp = [[0] * (m + 1) for _ in range(coin_count)]
    for i in range(len(coins)):
        dp[i][0] = 1

    for money in range(1, m + 1):
        dp[0][money] = 1 if money % coins[0] == 0 else 0

    for i in range(1, len(coins)):
        coin = coins[i]
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if j - coin >= 0:
                dp[i][j] += dp[i][j - coin]

    # print_table(dp)
    print(dp[len(coins) - 1][m])




