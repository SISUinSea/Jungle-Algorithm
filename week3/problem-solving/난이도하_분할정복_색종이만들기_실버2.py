# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

"""
# 모든 칸을 조사하면서, 모두 같은 색깔이라면 해당 색의 종이이다. 해당 색 종이 count 를 ++
# 아닌 경우에는, 4등분해서 모든 두 같은 색의 종이인지 확인하는 재귀함수를 짠다.
## 중요한 것은 2차원 배열에서의 index 컨트롤이다.
"""
def determine_color(size, si, sj):
    global blue_count, white_count, p
    color = p[si][sj]
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            if p[i][j] != color:
                determine_color(size//2, si, sj)
                determine_color(size//2, si + size // 2, sj)
                determine_color(size // 2, si, sj + size // 2)
                determine_color(size // 2, si + size // 2, sj + size // 2)
                return

    if color == 0:
        white_count += 1
    else:
        blue_count += 1


blue_count = 0
white_count = 0
# N 입력받기
n = int(input())

p = [list(map(int, input().split())) for _ in range(n)]

determine_color(n, 0, 0)

print(white_count)
print(blue_count)