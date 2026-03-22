# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
# 군대에서 풀었던 그 문제... 기억이 난다. 그 때가 그립진 않지만.... 그 때의 나, 그 시간이 흘러가버림에 너무나 큰 아쉬움을 느낀다....
#




from collections import defaultdict

d = defaultdict(list)

d[1].append(123)


print(d)



def solution(src=1):
    count = 0
    visited = [0] * (c + 1)
    stack = [src]

    while stack:
        computer = stack.pop()
        if visited[computer] == 1:
            continue
        visited[computer] = 1
        count += 1
        for v in adj[computer]:
            stack.append(v)

    return count - 1 ## src를 count 한 것을 빼줌


c = int(input())
e = int(input())


adj = {node : [] for node in range(c + 1)}

for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

print(solution())