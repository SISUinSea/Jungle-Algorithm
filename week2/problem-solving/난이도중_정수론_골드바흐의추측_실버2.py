# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
"""
1. 무엇을 구하나?
- 어떤 짝수를 두 소수의 합으로 나타낼 수 있는 그 소수들을 출력해야 함.

2. 입력 / 출력
- 입력: (각 테스트 케이스마다) 짝수 정수
- 출력: 더해서 그 수가 되는 소수 두 개 (작은 것 먼저, 큰 것 나중)

3. 핵심 제약
- n <= 10,000
- 여러 가지가 있는 경우에는 소수의 차이가 가장 적은 것부터 출력해야 한다..!!

4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 <<  >> 문제다.

6. 접근
- 1. 소수들을 모아놓은 리스트를 만든다.
- 2. 주어진 수보다 작거나 같은 수들을 담은 작은 리스트를 만든다.
- 3. 여기서 두 개를 고르는 조합을 만든다.
- 4. 보통 나중에 추가된 조합이 두 수의 차이가 작다. 조합 리스트를 거꾸로 뒤집는다.
- 5. 하나씩 계산한다.

** Batch로 접근했을 때 시간 초과가 뜨지는 않을까? T의 개수가 안 주어졌는데...
** 조합 리스트를 만드는데 걸리는 시간 복잡도는? C(10,000, 2) ~~= 10^8



6.2 다른 접근!! -> ? -> (x)
** 핵심 아이디어 : 굳이 조합을 안 만들어도 된다!! 소수 리스트만 만들면 거기 안에서 시도하면 된다고 생각했는데.. 일단 아이디어는 이렇다.
1. n // 2에서 시작, 가장 가까운 소수들을 찾는다.(딱 그 절반이 소수라면 거기서 종료)
2. 아니라면 오른쪽/왼쪽으로 한 칸씩 포인터를 이동시키면서 그 합이 해당 짝수인지 찾는다.
(??) 하지만 이 방법은 모든 짝수가 소수의 2배이거나, 절반에서 같은 개수만큼 떨어진 짝수인 경우에만 작동한다. 반례는 ... 있나?
있다.
100.
50의 양 옆의 수는
47, 53....? 엥??/ 이건 반례가 아니었다.

굳이 반례를 안 찾아도, 모든 인접한 소수의 차이가 같은게 아니기 때문에 사용할 수 없는 전략이다.


그럼 다시 6. 접근으로 돌아가서...

시간 복잡도가 괜찮은 것인가?

정확하지는 않지만... 괜찮아보인다. 결국.. 10^8 번 호출...??? time limit이 아니라 memory limit에 대해 신경써야 한다.
파이썬에서 함수 하나의 오버헤드가 어느 정도일까?

근데 생각해보면 선택해야 하는 개수 k 가 2로 고정되어 있기 때문에 굳이 재귀를 사용하지 않아도 된다.

고민 끝!!! 구현으로 가기 위한 다음 단계를 밟자.


마지막 하나 더!! time limit에 걸리지 않는 전략인지 검토해보자.
그냥 갔으면 큰일날뻔... time limit에 걸린다. 10,000 * 10,000 = 10^8니까 2초 시간 제한 안에 못 푼다.
그럼 조합을 이렇게 만드는게 아니라는 말 같은데...? 아니면??? Batch로 안 하고 그때그때 하나씩 해보면 안 되나..? 왜냐면
뭔가 골드바흐 추측에서 이런 짝수들이 2, 어떤 큰 수 이렇게는 안 나오는 것 같은데??? 하지만 이건 그냥 넘겨짚기야...

귀납적으로... 모든 조합을 안 만들어도 되는 것 같은데...??? 근데 이런 찜찜한 상태로 구현을 시작해도 되는건가?
근데 시험이었다면 그냥 무작정 구현했을 것 같기는 함....ㅠㅠ

하지만 내가 해본 사례에서는 이런 규칙을 보인다.

절반으로 나눴을 때 짝수다 ->

7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [ ] 전략을 사용해서 예제를 풀 수 있다.
- [] 왜 이 접근인지 설명할 수 있다 -> 그냥 귀납적으로 그래 보인다.... 는 안 되는거잖아. 반례가 하나 존재할 수 있는데?



8.0 푸는 중...
내가 세운 전략이 틀렸다. 이렇게 실컷 구현해놓은 다음에 반례 등을 찾아버리면 너무 힘들어지기 때문에 전략을 예제로 검증하는 단계를 꼭 거쳐야 한다는 것을 배웠다.
8. 풀고 난 뒤
-

"""

# half 인자가 소수 테이블에서 어떤 prime_table[index] 값들 사이에 있는지 찾는다.
# 그 값을 index로 반환한다.
# index는 prime_table[index - 1] <= half <= prime_table[index] 를 만족하는.. 수다.
# 이게 유일하다고 어떻게 말할 수 있지? -> A 구간과 B구간이 절대 겹치지 않기 때문에 A 구간에 속한다면 B 구간에 속하지 않음이 명확하게 드러난다.
def find_index(half):
    global primes
    for i in range(0, len(primes)):
        if half <= primes[i]:
            return i
    return -123 # 이게 나올 일은 없지만.... 방어적으로 하자.

# 10,000보다 작은 소수들을 모아놓은 리스트를 만든다. 에라토스테네스의 체를 사용한다.
## boolean prime table 만들기
prime_table = [True for _ in range(10_000 + 1)]
prime_table[0] = False
prime_table[1] = False
## prime table 완성하기
for i in range(2, 5_000):
    if not prime_table[i]:
        continue
    for j in range(i * 2, 10_000 + 1, i):
        if j > 10_000: break
        prime_table[j] = False


## prime이면 primes list 에 추가하기
primes = [-1]
for i in range(2, 10_000+1):
    if prime_table[i]:
        primes.append(i)

# print(len(primes))
# return
t = int(input())
for _ in range(t):
    # 짝수를 절반으로 나눈다.
    n = int(input())
    # print(n, end = ": ")
    half = n // 2
    ## 짝수인 경우
    ### 1. 양쪽 기준을 두 개 설정한다. 이름은 left_std, right_std
    left_std_index = find_index(half) - 1
    right_std_index = left_std_index + 1

    # print(f"left index: {left_std_index}, right index: {right_std_index}")
    # print(f"left: {primes[left_std_index]}, right: {primes[right_std_index]}")
    # print(f"{primes[left_std_index]}, {primes[3+1]}")
    while True:
        if half in primes:
            print(half, half)
            break
        left = primes[left_std_index]
        right = primes[right_std_index]
        sum = left + right
        if sum == n:
            print(left, right)
            break
        elif sum < n: right_std_index += 1
        elif sum > n: left_std_index -= 1


    #### 어느 인덱스에 위치하는지 찾아야 한다.
    ### 2. 칸 수를 늘려가며 각 기준에서 오른쪽, 왼쪽 칸만큼들의 수를 합해서 해당 수인지 확인한다.
    #
    # ## 홀수인 경우
    # else:
    # ### 1. 소수인지 확인한다. lucky!
    #     if half in primes:
    #         print(half, half)
    #         continue
    # ### 2. 아니라면, 사이 그 지점을 std로 잡고, 1칸씩 칸수를 늘려가며 양 옆의 합이 해당 수인지 확인한다.
    #     else:
    #         std_index = find_index(half)
    #         for gap in range(1, 5000):
    #             if primes[std_index - gap] + primes[std_index + gap] == n:
    #                 print(primes[std_index - gap], primes[std_index + gap])
    #                 break
