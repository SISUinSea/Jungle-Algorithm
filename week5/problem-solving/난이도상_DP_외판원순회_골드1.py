# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098

INF = 1_000_000 * (16 + 1)
src = 0

def solve(cur, visited_mask, memo):
    # print(cur, visited_mask)
    """
    Args:
        cur: 현재 위치
        visited_mask: 방문한 노드(cur 포함)

    Returns:
        현재 위치에서 시작 노드(0)까지 남은 노드들을 모두 거쳐 돌아가는 비용(불가능하면 INF)

    Base Case:

    """
    if memo[cur][visited_mask] is not None:
        return memo[cur][visited_mask]


    if visited_mask == (1 << n) - 1:
        return INF if w[cur][src] == 0 else w[cur][src]

    memo[cur][visited_mask] = INF
    for adj, cost in enumerate(w[cur]):
        if cost == 0: # 방문할 edge가 없는 경우
            continue
        if visited_mask & (1 << adj): # 이미 방문한 경우
            continue
        memo[cur][visited_mask] = min(memo[cur][visited_mask], cost + solve(adj, visited_mask | (1 << adj), memo))
    return memo[cur][visited_mask]




n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

memo = [[None] * (1<<n) for _ in range(n)]
print(solve(0, 1, memo))
