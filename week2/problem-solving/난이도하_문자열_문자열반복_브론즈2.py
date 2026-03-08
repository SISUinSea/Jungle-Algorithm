# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
t = int(input())
answer = ""

for _ in range(t):
    i1, i2 = map(str, input().split())
    r = int(i1)
    s = i2
    for i in range(len(s)):
        for _ in range(r):
            answer += s[i]
    answer += "\n"

print(answer)
