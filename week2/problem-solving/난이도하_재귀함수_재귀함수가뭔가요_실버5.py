# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478
"""
1. 무엇을 구하나?
- 재귀함수의 호출을 indentation으로 보여주는 출력을 구현해야 한다.

2. 입력 / 출력
- 입력: 재귀 깊이
- 출력: 해당 깊이만큼 출력된 재귀 이야기(indentation으로 구분됨)

3. 핵심 제약
- 재귀 깊이는 50 이하...

4. 예제 설명
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.<<는 시작할 때 추가.
함수에서는
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
를 순서대로 호출한다.
각 문장 앞에 arg로 넘겨받은 depth 변수에 따라 indentation을 추가한다.


5. 한 줄 요약
- 결국 이 문제는 << 몇 번째로 호출된 재귀인가에 따라 indentation을 문장과 붙이는 >> 문제다.

6. 접근
- base case 조건은... depth가 limit이 되었을 때. 행동은 아무것도 하지 않고 반환.
-

7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [x] 왜 이 접근인지 설명할 수 있다

8.1 푸는 중
- 또또또 문제 제대로 안 읽었다!!!! base case 의 action은 "재귀함수는 자기 자신을 호출하는 함수라네" 출력이다.

8.2 풀고 난 뒤
- 하지만... 풀면서 그런 사소한 디테일을 잡아낼 수 있는 거 아닐까?? 꼭 문제를 구현하기 전 모든 것을 알고 들어갈 필요가 있나?

"""
indentation = "____"
base_case_text = '"재귀함수는 자기 자신을 호출하는 함수라네"\n'
answer_start_text = '"재귀함수가 뭔가요?"\n'
answer_texts = [
    '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n',
    '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n',
    '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n',
]
answer_end_text = "라고 답변하였지.\n"

def response_recursive_answer(depth, limit):
    global result
    result += indentation * depth
    result += answer_start_text
    if depth == limit:
        result += indentation * depth
        result += base_case_text
        result += indentation * depth
        result += answer_end_text
        return

    for answer_text in answer_texts:
        result += indentation * depth
        result += answer_text

    response_recursive_answer(depth + 1, limit)

    result += indentation * depth
    result += answer_end_text


global result

result = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n"


limit = int(input())
response_recursive_answer(0, limit)
print(result)