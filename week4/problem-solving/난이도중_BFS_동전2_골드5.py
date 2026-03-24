# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294



"""
k 크기의 arr를 만든다. index는 동전(들)을 가지고 만들 수 있는 가격, arr[index]는 몇 개의 동전으로 그 가격을 만드는지를 저장한다.

각 동전들을 큐에 저장한다.


큐가 빌 때까지 반복한다.

큐에서 값을 꺼내, 거기에 동전을 하나씩 더해서 만들 수 있는 가격(index)에 현재의 값에서 동전을 하나 더했을 때의 값이 더 작다면 업데이트 한다.
그 가격이 arr의 크기를 넘어가면 생략한다.
그 값이 이미 있는 값보다 크다면 생략한다.
arr[k]에 값이 업데이트 되었을 때, 그 값이 최솟값임을 보장할 수 있다. -> (어떻게?) 따라서 프로그램을 종료한다.


"""
from collections import deque, defaultdict

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp_table = defaultdict(int)

queue = deque(coins)
for coin in coins:
    if coin == k:
        print(1)
        exit()
    dp_table[coin] = 1

while queue:
    val = queue.popleft()
    for coin in coins:
        new_val = val + coin
        if new_val > k: continue
        if new_val in dp_table: continue
        # if dp_table[new_val] > dp_table[val] + 1:
        dp_table[new_val] = dp_table[val] + 1
        # ?    queue.append(new_val)

        if new_val == k:
            print(dp_table[new_val])
            exit()
        queue.append(new_val)

print(-1)
