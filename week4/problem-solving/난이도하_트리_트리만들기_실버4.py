# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244




n, m = map(int, input().split())

print(0, 1)
m -= 1
i = 2
before = None
for i in range(i, n):
    if m > 0:
        print(1, i)
        m -= 1
    else:
        print(i - 1, i)
