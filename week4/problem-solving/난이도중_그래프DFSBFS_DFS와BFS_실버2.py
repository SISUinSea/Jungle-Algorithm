# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque

def bfs(src, adj, visited):
    queue = deque([src])
    visited[src] = True
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for dst in adj[node]:
            if visited[dst]: continue
            visited[dst] = True
            queue.append(dst)

    return result


def dfs(src, adj, visited):
    stack = [src]
    result = []

    while stack:
        node = stack.pop()
        if visited[node] : continue
        visited[node] = True
        result.append(node)
        for dst in reversed(adj[node]):
            if visited[dst]: continue
            stack.append(dst)

    return result


N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N + 1):
    adj[i].sort()

visited = [False] * (N + 1)
print(*dfs(V, adj, visited))

visited = [False] * (N + 1)
print(*bfs(V, adj, visited))

