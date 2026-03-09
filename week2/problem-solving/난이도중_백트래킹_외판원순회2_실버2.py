# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
"""
1. 무엇을 구하나?
- 외판원이 도시를 중복하지 않게 순회할 수 있을 때 순회에 필요한 최소 비용

2. 입력 / 출력
- 입력: i -> j 이동 비용(행렬로 주어짐)
- 출력: 최소 비용

3. 핵심 제약
- 갈 수 없는 경로의 경우 0으로 주어진다. 비용이 0이라는 게 아님에 주의 해서 구현 해야 한다.
- N <= 10이므로 10!= 3,600,000 정도다(대략)...


4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 << 방문 순서를 순열로 뽑아 각 비용을 계산하는 완전탐색 >> 문제다.

6. 접근
- 모든 도시를 순서를 고려해서 중복되지 않게 뽑는 조합을 구현한다.
- 각 조합 리스트를 만들면 바로 검사해서 메모리 공간을 절약한다.

7. 구현 시작 전 체크
- [ ] 문제를 제대로 이해했다
- [ ] 예제를 설명할 수 있다
- [ ] 왜 이 접근인지 설명할 수 있다

8. 푸는 도중...
-

9. 풀고 난 뒤
-

"""

def calculate_cost():
    global W, routes
    cost = 0
    for i in range(0, len(routes) - 1):
        src, dest = routes[i], routes[i+1]
        weight = W[src][dest]
        if weight == 0:
            return VERY_BIG_INTEGER # 매우 큰 수. 절대로 답이 될 수 없어야 한다.
        cost += weight
    if W[routes[-1]][routes[0]] == 0:
        return VERY_BIG_INTEGER
    cost += W[routes[-1]][routes[0]]
    return cost

def make_order():
    global routes, n, answer
    if len(routes) == n:
        answer = min(answer, calculate_cost())

    for i in range(0, n):
        if i in routes: continue
        routes.append(i)
        make_order()
        routes.pop()



VERY_BIG_INTEGER = 310_000_000_000_000
n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
routes = []
answer = 310_000_000_000_000


make_order()

print(answer)