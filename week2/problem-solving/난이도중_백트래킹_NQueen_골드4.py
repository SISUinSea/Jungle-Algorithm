# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
"""
1. 무엇을 구하나?
- Q을 놓을 수 있는 경우의 수

2. 입력 / 출력
- 입력: N 보드의 수, 놓아야 하는 퀸의 수
- 출력: 퀸이 서로를 공격하지 않으며 보드에 올라갈 수 있는 경우의 수

3. 핵심 제약
- N < 15, 모든 경우를 찾으며 백트래킹으로 푸는 문제..

4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 << 좌표를 압축해서 퀸이 서로를 공격하지 않으며 보드에 올라갈 수 있는 경우의 수를 찾는 >> 문제다.

6. 접근
- 어느 퀸이 놓인 자리 i, j와 자리가 겹치는 자리는 다음의 조건 중 하나를 무조건 만족한다.
    1. 차(i - j) 값이 동일하다.
    2. 합(i + j) 값이 동일하다.
    3. i 좌표 값이 동일하다.
    4. j 좌표 값이 동일하다.
- 따라서 전체 2차원 배열에서의 겹침 여부를 확인할 필요 없이 각각의 리스트 4개를 사용하면 겹침 여부를 쉽게 확인할 수 있을 것이다.

- 모든 좌표를 n 번 순회하며 조합을 만든다.
- 각 조합에 대해 겹치는지 평가한다.
- 겹치지 않는다면 cnt ++

- 겹침은 어떻게 평가하는가?
    - 네 리스트에서 겹치는 값이 있는지 각각 검사한다.
    - 겹치는게 없다면 네 리스트 각각에 요소를 추가한다.


7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [x] 왜 이 접근인지 설명할 수 있다

8. 푸는 도중...
- 아.... 근데 i, j를 array[i] = j로 차원을 압축한다고 했을 때 매 array의 index에 최대 15개를 각각 검색하려면 n^n????
    > 근데 층을 내려가면서 뭔가 많이 배제될 것 같은데....? 그럼 n!; 15! ~= 10^12

9. 풀고 난 뒤
-

"""

def backtrack(i):
    global n, answer, diffs, sums, ys
    # print(ys)

    if len(ys) == n:
        answer += 1
        return
    for j in range(0, n):
        # i 번째에 넣을 값을 정하기 :positions[i] = ?
        if (
            j in ys or
            i + j in sums or
            i - j in diffs
        ):
            continue
        ys.append(j)
        sums.append(i + j)
        diffs.append(i - j)

        backtrack(i + 1)

        ys.pop()
        sums.pop()
        diffs.pop()


n = int(input())

diffs = []
sums = []
ys = []


answer = 0

backtrack(0)

print(answer)