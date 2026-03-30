# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

"""
# [문제명]

- 링크:
- 분류:
- 결과:

## 1. 문제 이해
- 한 줄 요약: adj를 s, s+1, s-1로 하는, 최단 경로를 찾는 문제.
- 핵심 조건: 방문할 수 없는 지점도 있다.

### 입력 계약
- 보장되는 것: 출발지와 도착지는 방문할 수 있다. 출발지에서는 무조건 1칸만 점프할 수 있다.
- 안 나오는 것:
- 내 코드 분기를 바꾸는 입력 형태:

## 2. 접근
- 처음 접근: visited 정수 배열과 queue를 쓰는 bfs 방식으로 풀면 되는거 아닌가 싶은데.....? 이렇게 풀었을 때의 풀이 정당성을 확보해보자.
- 최종 접근: 근데 한 큐를 처리할 때 최적값보다 먼저 visited에 값을 쓸 수가 있다. min으로 최적값을 업데이트 해야 한다. 또 그럴 때에만 enque 해야 한다.
- 왜 맞는가:
- 아직 불안한 부분: 이렇게 했을 때 정답이 나오는지...?

## 3. 설계
- 자료구조: deque
- 핵심 로직:
    1. 첫 번째 노드를 enque하고 visited 처리 한다.
    2. 큐가 빌 때까지 다음을 반복한다.
        3. node, speed = deque
        4. node에서 각각 s + 1, s, s - 1만큼 점프한 노드에 대해서
            아예 방문할 수 없는 노드라면 넘어간다.
            방문하지 않은 노드라면 방문처리한다.
            아니라면, 현재 값이 최소값 일때에만 방문처리한다.
                5. 방문처리했을 경우에만 enque

    아니 이거 로직을 이렇게 허술하게 짜도 되는건가???

- 예외 처리:
- 복잡도:


### 새로운 전략 설계 (이전 것은 틀렸음)
- 자료구조: 2D array(위치, 속도를 인덱스로 하는)
- 핵심 로직: 방문을 처리하기 위해서 큐를 사용한다.(이론상 스택을 사용해도 풀 수 있는 문제이다.) 큐가 빌 때까지 반복한다.
            큐에서 dequeue한 뒤 탐색은 다음을 따른다.
                1. 해당 속도에서 방문할 수 있는 새로운 노드들을 탐색한다. (방문하지 않았거나, 내가 방문하는게 더 빠른 경우에만 큐에 넣는다. 큐에 넣는 시점에 방문처리 해도 괜찮다.)

    상태:             (위치, 속도), visited[index][speed]는 해당 위치에, 해당 속도로 방문할 수 있는 최소 점프 횟수를 나타낸다.
    시작 상태:         (2, 1)
    다음 상태:         index + speed; speed => [speed - 1, speed, speed + 1]
    버릴 조건:         위치가 목표 위치보다 클 때,
                     stride가 0이거나 더 작을 때,
                     visited에 이미 더 작은 값이 업데이트 되어 있을 때,
                     위치가 금지 돌일 때
    갱신 조건:         visited에 한 번도 방문한 적 없거나 내가 계산한 값이 더 작을 때
    정답 추출:         큐가 다 빈 뒤, 목표 위치의 여러 속도로 도달한 값 중 최소값

    BFS(Queue)를 사용해서 순회한다고 했을 때, 처음 갱신된 값이 최소 점프 횟수임을 보장할 수 있는가?
    있다. 이유는 다음과 같다.

    - 속도 speed의 최댓값을 뭐라고 해야 할까? 1 + 2 + ... + S ~= 10,000이 되는 S를 찾으면 된다.
    - S 는 대략 141 정도로 잡으면 충분히 커버가 가능하다.


### DP
- 상태: dp[index][speed] -> index 위치에서 speed로 도달했을 때의 최소 점프 횟수
- 점화식: dp[new_index][new_speed] = min(dp[new_index][new_speed], dp[index][speed] + 1)
- 초기값: dp[2][1] = 1이다. 방문하지 않은 칸들은 충분히 큰 값으로 초기화 해야 한다.

## 4. 검증
- 손검산:
- 분기 테스트:
- 반례:

## 5. 실수 / 디버깅
- 증상:
- 실제 원인:
- 놓친 계약/분기:
- 다음엔 어디서 체크할지:

## 6. 교훈
-

## 7. 백로그
-
"""
INF = 100_000 + 1
from collections import deque

n, m = map(int, input().split())  # n: 목표지점, m: 작은 돌 개수
no_rocks = set()
for _ in range(m):
    no_rocks.add(int(input()))

dp = [[INF] * (141 + 1) for _ in range(n + 1)]

queue = deque()
queue.append((1, 0))
dp[1][0] = 0

while queue:
    node, speed = queue.popleft()
    for stride in [speed - 1, speed, speed + 1]:
        if stride <= 0: continue

        adj = node + stride
        if adj > n: continue
        if adj in no_rocks: continue
        if dp[adj][stride] != INF: continue

        queue.append((adj, stride))
        dp[adj][stride] = dp[node][speed] + 1

answer = INF
for i in range(1, len(dp[0])):
    answer = min(answer, dp[n][i])
if answer == INF: answer = -1

print(answer)



