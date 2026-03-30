# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865


"""
# [문제명]

- 링크:
- 분류:
- 결과:

## 1. 문제 이해
- 한 줄 요약: 한계 용량보다 작게 배낭을 꾸렸을 때 가치를 최대화해야 하는 조합을 찾아내야 한다.
- 핵심 조건:

### 입력 계약
- 보장되는 것: N <= 100, K <= 100,000
- 안 나오는 것: 입력으로 주어지는 수는 모두 정수
- 내 코드 분기를 바꾸는 입력 형태: 분기는 딱히 없다.

## 2. 접근
- 처음 접근: 최적해를 찾는 함수를 f(k, arr, i) 라고 했을 때 해당 값은 i번째 짐을 넣었을 때와 넣지 않았을 때의 배낭의 최대 가치를 비교해서 구할 수 있다.
            그렇게 했을 시 구조가 같은 subproblem으로 나눌 수 있다.
            k, i에 대한 2차원 배열을 저장해놓고 값을 재활용 할 수 있다.
- 최종 접근: Top-down 재귀와 DP table을 사용한다.
- 왜 맞는가:
    최악의 경우 100,000*100 = 10,000,000 번의 공간과 연산이 필요하다.
    그 정도면 파이썬으로도 풀 수 있어 보이는데....?


- 아직 불안한 부분:

## 3. 설계
- 자료구조: dict나 defaultdict를 써보고 싶었으나 2차원 배열을 어떻게 나타내야 할지 모르겠어서 일단은 2차원 배열을 그대로 사용한다.
- 핵심 로직:
- 예외 처리:
- 복잡도: 최악의 경우에도 10,000,000(천만)번의 공간과 연산을 하면 된다.

### DP
- 상태: dp[i][k] = 남은 용량 k와 i 이후 물건들만 가지고 만들 수 있는 최대 가치
- 점화식:
    현재의 물건을 배낭에 넣을 수 없을 때(item.weight > k)
    dp[i + 1][k] = dp[i][k],
    있을 때
    dp[i + 1][k] = max(
- 초기값:

## 4. 검증
- 손검산:
- 분기 테스트:
- 반례:

## 5. 실수 / 디버깅
- 증상: Index Error... 어디서 난거지??????
- 실제 원인:
- 놓친 계약/분기:
- 다음엔 어디서 체크할지:

## 6. 교훈
-

## 7. 백로그
-
"""


def solution(K, arr, i, dp=None):
    if not dp:
        dp = [[0]*(K + 1) for _ in range(len(arr) + 1)]
        # print(dp)
    # k == 0이면(배낭에 더이상 물건을 담을 수 없으면) return 0
    if K <= 0:
        return 0
    # i가 arr을 초과했으면 return 0
    if len(arr) <= i:
        return 0
    # 이미 계산된 값이 존재한다면 return 0
    if dp[i][K] != 0:
        return dp[i][K]

    for item in arr[i:]:
        weight, value = item
        # item을 넣을 수 없는 상태라면 넘어가기
        if K - weight < 0:
            continue
        dp[i][K] = max(dp[i][K], max(value + solution(K - weight, arr, i + 1, dp), solution(K, arr, i + 1, dp)))

    return dp[i][K]


# 입력값 처리
n, k = map(int, input().split())
items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
items.sort(key=lambda x: (x[0]), reverse=True)

print(solution(k, items, 0))













