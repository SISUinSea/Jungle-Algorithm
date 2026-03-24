# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
from collections import deque

def adjs(i, j):
    result = []
    if 0 <= i + 1 < n and M[i + 1][j] == '1': result.append((i + 1, j))
    if 0 <= i - 1 < n and M[i - 1][j] == '1': result.append((i - 1, j))
    if 0 <= j + 1 < m and M[i][j + 1] == '1': result.append((i, j + 1))
    if 0 <= j - 1 < m and M[i][j - 1] == '1': result.append((i, j - 1))
    return result

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        pos = queue.popleft()
        si, sj = pos[0], pos[1]
        if si == n - 1 and sj == m - 1: return
        for adj in adjs(si, sj):
            x, y = adj
            if visited[x][y] != 0: continue
            visited[x][y] = visited[si][sj] + 1
            queue.append((x, y))


def print_visited():
    print("==================")
    for row in visited:
        print(*row)


n, m = map(int, input().split())



M = [list() for _ in range(n)]
for i in range(n):
    for c in input():
        M[i].append(c)
visited = [[0] * (m) for _ in range(n)]

bfs(0, 0, visited)

print(visited[n - 1][m - 1])

