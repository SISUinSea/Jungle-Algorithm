# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
from collections import deque

n = int(input())

m = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

# print(visited)
queue = deque()
queue.append((0, 0))

while queue:
    i, j = queue.popleft()
    if i == n - 1 and j == n - 1:
        print("HaruHaru")
        exit()
    if visited[i][j] == 1:
        continue
    visited[i][j] = 1
    stride = m[i][j]
    if i + stride < n:
        queue.append((i + stride, j))
    if j + stride < n:
        queue.append((i, j + stride))


print("Hing")