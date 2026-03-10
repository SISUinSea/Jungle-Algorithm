# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
"""
1. 무엇을 구하나?
- IPv6의 암호화된 버전을 디코딩해야 함

2. 입력 / 출력
- 입력: IPv6의 축약이되어 있을수도 있는 string
- 출력: IPv6의 축약을 완전히 다 풀어버린 string

3. 핵심 제약
-

4. 예제 설명
-

5. 한 줄 요약
- 결국 이 문제는 <<  >> 문제다.

6. 접근
- :: 으로 축약된 0을 몇 개로 복원해야 하는지 세야 한다.

- 해결
    1. ::을 제외하고 주어진 그룹이 몇 개 있는지 count
    2. ::이 있다면, 총 8개의 그룹에서 몇 개가 생략되었는지 역산, 복원
    3. 각 자리가 모두 4자리인지 검사, 아니라면 제일 앞자리에 0 붙이기(4자리가 될 때까지)

7. 구현 시작 전 체크
- [ ] 문제를 제대로 이해했다
- [ ] 예제를 설명할 수 있다
- [ ] 왜 이 접근인지 설명할 수 있다

8. 푸는 도중...
-

9. 풀고 난 뒤
-

"""

# 1. ::을 제외하고 각 그룹이 몇 개인지 count
## ::을 기준으로 좌, 우로 나눈다. 우변에 뭔가 있다면 ::이 있는거, 아니라면 없는 것...
ipv6 = input()
groups = []
# 2. ::이 있다면, 총 8개의 그룹에서 몇 개가 생략되었는지 역산, 복원
if "::" in ipv6:
    left, right = ipv6.split("::")
    left_group = left.split(":")
    right_group = right.split(":")

    groups.extend(left_group)
    for _ in range(8 - len(left_group) - len(right_group)):
        groups.append('')
    groups.extend(right_group)
else:
    groups = ipv6.split(":")


# print(groups)

decoded_groups = []

# 3. 각 자리가 모두 4자리인지 검사, 아니라면 제일 앞자리에 0 붙이기(4자리가 될 때까지)
for group in groups:
    if len(group) == 4:
        decoded_groups.append(group)
        continue
    else:
        decoded_groups.append('0' * (4-len(group)) + group)

print(":".join(decoded_groups))
