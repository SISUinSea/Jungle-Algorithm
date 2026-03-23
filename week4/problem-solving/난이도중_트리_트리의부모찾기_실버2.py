# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
from collections import defaultdict

n = int(input())
adj = defaultdict(list)
# print(n)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# print(adj)

parent = [0] * (n + 1)  ## parent를 스택처럼 쓰자.
stack = []

stack.append(1)
parent[1] = -1 ## 부모 없음

while stack:
    v = stack.pop()
    # print(v)
    for u in adj[v]:
        if parent[u] != 0:
            continue
        parent[u] = v
        stack.append(u)

for i in range(2, n + 1):
    print(parent[i])