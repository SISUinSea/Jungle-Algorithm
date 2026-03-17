# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
"""
1. 무엇을 구하나?
- 거듭제곱의 결과

2. 입력 / 출력
- 입력: 정수 A, B, C
- 출력: (A ^ B) % C

3. 핵심 제약
- B가 커지게 되면? 너무 큰 수를 곱해야 해서 시간 초과가 나는건가??? 잘 쪼갤 수 있는 방법을 생각해야 한다.
- 즉,

4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 <<  >> 문제다.

6. 접근
- 홀수인 경우, A * backtrack(B - 1) 로 호출한 함수가 짝수임을 보장하게 한다.
- B가 짝수인 경우, backtrack(B // 2) 를 한 번만 호출한다.

7. 구현 시작 전 체크
- [ ] 문제를 제대로 이해했다
- [ ] 예제를 설명할 수 있다
- [ ] 왜 이 접근인지 설명할 수 있다

8. 푸는 도중...
-

9. 풀고 난 뒤
- 이게 왜 맞음?????? 왜 그동안은 시간초과, 메모리 초과가 떴던거지??????

"""

def backtrack(a, b, c):
    if b == 1:
        return a
    if b % 2 == 0:
        half = backtrack(a, b // 2, c)
        half %= c
        return half ** 2
    else:
        return (a * backtrack(a, b - 1, c))
a, b, c = map(int, input().split())
print(backtrack(a, b, c) % c)

