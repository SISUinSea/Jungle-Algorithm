# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157


word = input().lower()
char_count = dict()
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# max value 저장.
max_value = 0
for char, count in char_count.items():
    if count > max_value:
        max_value = count

max_value_count = 0
max_word = ""
# max value인 key가 2개 이상이면 flag change
for char, count in char_count.items():
    if max_value == count:
        max_value_count += 1
        max_word = char

if max_value_count > 1:
    max_word = "?"
# result print
print(max_word.upper())