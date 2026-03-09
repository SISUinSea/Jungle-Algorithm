# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
"""
1. 무엇을 구하나?
- 주어진 입력값들을 적절히 배치해서 연산 결과를 최대화하기

2. 입력 / 출력
- 입력: 배열 크기, 배열에 들어있는 수들
- 출력: 주어진 연산 결과의 최댓값

3. 핵심 제약
- N <= 8, 8! = 40320. 완전 탐색으로 풀 수 있는 문제다.

4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 << 순열 만들기 >> 문제다.

6. 접근
- 순열을 만든다.
- 주어진 연산을 하며 최댓값을 매번 갱신한다.
- 최댓값을 출력한다.

7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [x] 왜 이 접근인지 설명할 수 있다

8. 푸는 도중...
- (1차 시도 후) 아주 재밌는 반례 발견
0 0 1 인 경우 0 1 0으로 배치했을 때 2가 나와야 하는데... 왜 안 그러지??

9. 풀고 난 뒤
- 풀기 전 점검했어야 하는 '핵심 조건'은 요소의 값이 중복될 수 있다.. 였다.
-

"""
def backtrack():
    global L, answer, n
    # print(L)
    if len(L) == n:
        # print(L)
        total = 0
        for i in range(0, n - 1):
            total += abs(nums[L[i]] - nums[L[i + 1]])
        # print(total)
        if answer < total:
            answer = total

    for i in range(0, n):
        if i in L: continue

        L.append(i)   # choose
        backtrack()        # search
        L.pop()             # unchoose


n = int(input())
nums = list(map(int, input().split()))

L = []
answer = -1


backtrack()

print(answer)













