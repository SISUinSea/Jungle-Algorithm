# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1]:
            return False

    return True


n = int(input())
words = []


for _ in range(n):
    words.append(input())


h = dict()

for word in words:
    if is_palindrome(word):
        print(word[len(word) // 2])
        exit()
    if word in h:
        h[word] += 1
    else:
        h[word] = 1

    reversed = word[::-1]
    if reversed in h:
        h[word] += 1
    else:
        h[word] = 1


for item in h.items():
    if item[1] == 2:
        word = item[0]
        print(len(word), word[len(word)//2])
        break