# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
"""
1. 무엇을 구하나?
- 뱀 게임에서 뱀이 언제 죽는지를 계산

2. 입력 / 출력
- 입력: 보드 크기, 사과 개수와 위치, 시간대별 뱀의 움직임 이벤트
- 출력: 뱀이 언제 죽는지

3. 핵심 제약
- 뱀은 벽에 닿거나, 자기 몸에 닿으면 죽는다.
- 다음의 것들을 고려해야 한다.
        1. 어느 방향으로 향할 것인지에 해당하는 방향정보 -> 방향 전환 이벤트를 검사해서 적절히 바꿔야 한다.
        2. 현재 머리가 어느 칸에 위치해있는지 정보 -> 시간이 지남에 따라 방향 정보를 참고해서 위치를 이동시킨다.
        3. 몸 전체의 정보를 담고 있는 queue, -> 그냥 탐색하면 O(n), 별도의 맵을 따로 만든다면 공간 복잡도를 희생하고 시간 복잡도를 O(1)으로 만들 수 있다.
        4. 몸 길이는 굳이 저장할 필요 없다.
- 0-based index를 사용한다. 따라서 주어지는 모든 좌표값을 -1 해서 저장하고 사용한다.

4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 <<  >> 문제다.

6. 접근
- 뱀의 움직임은 다음과 같다.
    1. 현재 방향을 참고해서 이동한다. deque.append, 맵에 해당 부분을 표시한다.
    2. 죽는 위치인지 확인한다(맵을 벗어났거나, 몸과 부딫힌 경우)
    3. 방향 전환 이벤트가 존재하는지 확인한다. 존재한다면 방향을 전환하도록 값을 변경한다.
    4. 사과를 먹었는지 확인한다.(사과를 먹었다면 현재 시각 움직임을 종료한다.)
    5. 사과를 먹지 않았다면 꼬리를 deque.popleft를 한 뒤, 맵에서 해당 부분을 지워 뱀의 몸이 위치하지 않음을 표시한다.

7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [x] 왜 이 접근인지 설명할 수 있다

8. 푸는 도중...
-

9. 풀고 난 뒤
-

"""

from collections import deque

def change_direction(turn:str):
    global direction
    if turn == "D": # 오른쪽으로 방향을 전환한다.
        if direction == [0, 1]: direction = [1, 0]
        elif direction == [1, 0]: direction = [0, -1]
        elif direction == [0, -1]: direction = [-1, 0]
        elif direction == [-1, 0]: direction = [0, 1]
    elif turn == "L":
        if direction == [0, 1]: direction = [-1, 0]
        elif direction == [-1, 0]: direction = [0, -1]
        elif direction == [0, -1]: direction = [1, 0]
        elif direction == [1, 0]: direction = [0, 1]


direction = [0, 1]
n = int(input())
apple_count = int(input())
apple_map = [] # 1차원 배열로 구성, 나중에 최적화 할 때 2차원 배열로 맵을 구현
for _ in range(apple_count):
    x, y = map(int, input().split())
    apple_map.append([x-1, y-1])

change_dir_events = dict()
change_dir_count = int(input())
for _ in range(change_dir_count):
    event_data = input().split()
    change_dir = event_data[1]
    change_dir_time = int(event_data[0])
    change_dir_events[change_dir_time] = change_dir

snake_head = [0, 0]
snake_body = deque([snake_head]) # todo. deque(snake_head) 라고 쓰면 어떻게 되는지 제대로 알아보자.

time = 0


while True:
    # 시간 증가시키기
    time += 1
    # 뱀을 이동시키기
    snake_head = [snake_head[0] + direction[0], snake_head[1] + direction[1]] # todo. 더 깔끔하게 쓸 수 있을 것 같은데...
    # 죽는지 확인하기
    i, j = snake_head
    if not (0<=i<n) or not (0<= j < n):
        print(time)
        break
    if snake_head in snake_body:
        print(time)
        break

    snake_body.append(snake_head)

    # 방향 이동 이벤트 있는지 확인하기
    if time in change_dir_events:
        change_direction(change_dir_events[time])

    # 사과 먹었는지 확인해서 몸 길이 수정, 이동 마침
    if snake_head in apple_map:
        apple_map.remove(snake_head)
    else:
        snake_body.popleft()

