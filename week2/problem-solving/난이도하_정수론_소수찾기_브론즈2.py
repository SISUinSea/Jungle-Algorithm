# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
"""
1. 무엇을 구하나?
- 주어진 N개 수 중에서 소수가 몇 개인지

2. 입력 / 출력
- 입력: N, N개의 수
- 출력: 그 중에서 소수가 몇 개인지

3. 핵심 제약
- N은 1,000보다 작다.

4. 예제 설명
- 1, 3, 5, 7이 소수로 주어졌을 때
- 최댓값인 7까지 소수 판별하는 boolean table을 완성한 뒤
- 1은 소수가 아니다.
- 각각 계산했을 때 3, 5, 7은 모두 소수이다. prime_count ++를 진행.

5. 한 줄 요약
- 결국 이 문제는 << 소수 개수를 찾는 >> 문제다.

6. 접근
-  에라토스테네스의 체를 쓰지 않아도 시간 제약(2초)에 걸리지 않지만, 써보겠다.

7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [x] 왜 이 접근인지 설명할 수 있다

8. 풀고 난 뒤
- 네 번의 시도.....?? brute force로 풀고 있다.. 전략을 세우고 한번에 깔끔하게 맞춰야 하는데!
- 끝 부분의 인덱스가 인덱스 초과를 띄우지는 않는지...
- 또 풀기 전에 핵심 로직인 에라토스테네스의 체를 어떻게 만들 것인지 생각했었어야 했다.

"""

n = int(input())
nums = list(map(int, input().split()))

# 에라토스테네스 체 만들기, 초기화
prime_length = max(nums) + 1
prime_table = [True for _ in range(prime_length)] # [0]은 사용하지 않는다.
prime_table[0] = False
prime_table[1] = False

# for i in range(1, prime_length):
#     print(i, prime_table[i])

# 에라토스테네스의 체 완성
for i in range(2, prime_length):
    if not prime_table[i]: continue
    for j in range(2, prime_length // i + 1):
        if i * j >= prime_length: break
        prime_table[i*j] = False

# 소수 검증하기
prime_count = 0
for num in nums:
    # print(f'{num} is prime? {prime_table[num]}')
    if prime_table[num]:
        prime_count += 1

# for i in range(1, prime_length):
#     print(i, prime_table[i])

print(prime_count)