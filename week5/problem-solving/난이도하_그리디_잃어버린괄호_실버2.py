
# 문자열을 순회하며 std_index 값을 찾는다.
# A 요소들의 합을 구한다. (첫 번째 - 의 왼쪽에 있는 모든 요소들의 합)
# B 요소들의 합을 구한다.(첫 번째 - 의 왼쪽에 있는 모든 요소들의 합)
# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

"""
# [문제명]

- 링크:
- 분류: 그리디
- 결과:

## 1. 문제를 내 언어로
- 처음 이해: 주어진 식에 적절한 괄호를 쳐서 결과값을 최솟값으로 만든다. 즉 주어진 연산 명령과 연산자의 연산 순서를 조작해서 최솟값을 만들기.
- 다시 읽고 수정:
- 내가 풀어야 하는 질문 1문장:

## 2. 접근 + 정당성
- 처음 접근: - 부호 사이 + 연산들을 먼저 계산한다. 그 뒤 - 연산을 계산한다.
- 왜 된다고 생각했나: - 연산 앞에 올 연산자는 작아야 좋은 것 아닌가? 하는 생각이 들었지만 다음과 같이 위 전략이 최적해를 보장함을 알 수 있다.
                    1. - 연산 앞에 별도의 연산이 없다면 dont care
                    2. + 연산이 앞에 있었다면 dont care
                    3. - 연산이 앞에 있다면 + 들을 먼저 계산해서 - 연산의 right operand를 키워야 최솟값을 만들 수 있다.

- 최종 접근:
- 왜 맞는가:

## 3. 푸는 도중 든 생각
-
-
-

## 4. 설계
### Greedy
- 선택 기준:
- 정렬 기준:
- 성립 이유:

### 풀이
1. 먼저 + 연산을 전부 수행한다.
2. 이후 - 연산을 전부 수행한다.

## 5. 실수
- trial 1: TypeError. 어디서 났을까? -> 입력 예제가 -10인 경우..를 처리했다고 생각했는데...
- trial 2: TypeError. -> 10 + 20 같이 -가 아예 없는 경우 right expression에서 빈 값이 주어져서 에러.

왜 이거 생각을 못한거임?? edge case는 무조건 계산하고 가야 하는거였고 그렇게 떠올리기 어려운 엣지 케이스도 아니잖아.
당연히 검증하고 가야 하는거 아냐?
논리적 설계 단계에서는 문제가 없었지만 구현 단계에서 타입 오류를 체크했어야 했다.

## 6. 검증 / edge case
- 손검산:
- 반례1:
- 반례2:
- 반례3:

## 7. 교훈
- 구현한 뒤 엣지케이스의 경우 어떻게 되는지를 생각해보자.

## 8. 백로그
- 정규표현식 re 라이브러리를 안 쓰고 raw 구현으로만 풀어내는 건 어때?
"""

expression = input()

parts = expression.split("-")

result = sum(map(int, parts[0].split("+")))
for part in parts[1:]:
    result -= sum(map(int, part.split("+")))

print(result)


#
# import re
#
# expression = input()
# std_index = 0 # 첫 번째 -를 찾아 인덱스 값을 반환한다. 없다면 n + 1을 반환한다. n은 len(expression)
# # 문자열을 순회하며 std_index 값을 찾는다.
# for std_index in range(len(expression)):
#     if expression[std_index] == '-': break
# if std_index == len(expression) - 1: std_index = len(expression)
#
# # A 요소들의 합을 구한다. (첫 번째 - 의 왼쪽에 있는 모든 요소들의 합)
# if std_index == 0:
#     left_value = 0
# else:
#     left_expression = expression[:std_index]
#     left_operands = map(int, left_expression.split("+"))
#     left_value = sum(left_operands)
# # B 요소들의 합을 구한다. (첫 번째 - 의 오른쪽에 있는 모든 요소들의 합)
# if std_index == len(expression):
#     right_value = 0
# else:
#     right_expression = expression[std_index + 1: ] if std_index + 1 < len(expression) else []
#     right_operands = map(int, re.split(r"[-,+]", right_expression))
#     right_value = sum(right_operands)
#
#
# print(left_value-right_value)












