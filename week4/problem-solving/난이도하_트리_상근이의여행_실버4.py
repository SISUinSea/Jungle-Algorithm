# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    graph = {node : [] for node in range(n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(n - 1)

