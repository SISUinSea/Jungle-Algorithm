# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
n = int (input())

s = set()
a = []
for _ in range(n):
    d = int(input())
    a.append(d)

a.sort(reverse=True)


for element in a:
    for element2 in a:
        s.add(element + element2)


# 가장 큰 수부터 탐색하기, 답을 찾으면 종료
## 가장 큰 수 - 어떤 수 in {2쌍의 합} 이면 반환 후 종료


for target in a:
    for j in a:
        if target - j in s:
            print(target)
            exit()