# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251


"""
# 접근
점화식은 last character 가 같은지 여부를 두고 비교하면 된다.

"""

import sys
sys.setrecursionlimit(10**4 + 1)

def get_lcs_length(s1:str, s2:str, l1:int, l2:int, memo=None)->int:
    """

    Args:
        s1: 첫 번째 문자열
        s2: 두 번째 문자열
        l1: 첫 번째 문자열에서 비교할 마지막 인덱스
        l2: 두 번째 문자열에서 비교할 마지막 인덱스
        memo: l1, l2일 때의 LCS 값을 적어놓은 2차원 테이블

    Returns:
        l1, l2 부터 첫 번째 요소까지 비교했을 때의 LCS 길이(int)
    """
    if memo is None:
        memo = [[-1] * (l2 + 1) for _ in range(l1 + 1)]

    if l1 < 0 or l2 < 0:
        return 0

    if memo[l1][l2] != -1:
        return memo[l1][l2]

    if s1[l1] == s2[l2]:
        memo[l1][l2] = get_lcs_length(s1, s2, l1 - 1, l2 - 1, memo) + 1
    else:
        memo[l1][l2] = max(
            get_lcs_length(s1, s2, l1 - 1, l2, memo),
            get_lcs_length(s1, s2, l1, l2 - 1, memo)
        )
    return memo[l1][l2]



s1 = input()
s2 = input()

print(get_lcs_length(s1, s2, len(s1) - 1, len(s2) - 1))


