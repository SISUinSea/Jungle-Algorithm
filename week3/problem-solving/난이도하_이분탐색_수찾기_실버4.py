# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920


'''
정렬된 배열을 탐색하므로 binary search 사용
'''
def is_exist(q:int, arr):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == q:
            return True
        if arr[mid] < q: # left, m, q, right
            l = mid + 1
        elif arr[mid] > q:
            r = mid - 1

    return False

n = int(input())
A = list(map(int, input().split()))

m = int(input())
queries = list(map(int, input().split()))

A.sort()

for q in queries:
    print(1 if is_exist(q, A) else 0)