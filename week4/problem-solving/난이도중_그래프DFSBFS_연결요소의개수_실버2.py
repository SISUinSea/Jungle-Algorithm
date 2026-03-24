# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
def dfs(src):
    global count
    stack = [src]

    while stack:
        node = stack.pop()
        if visited[node] == 1: continue
        visited[node] = 1
        for v in adj[node]:
            if visited[v] == 1: continue
            visited[v] = 1
            stack.append(v)


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (n + 1)

count = 0

for i in range(1, n + 1):
    if visited[i] == 1:
        continue
    dfs(i)
    count += 1


print(count)