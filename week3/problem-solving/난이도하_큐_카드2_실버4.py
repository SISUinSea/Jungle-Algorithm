# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

deck = deque(range(1, int(input()) + 1))

i = 1
while len(deck) > 1:
    if i % 2 == 1: # 홀수인 경우 카드 버리기
        deck.popleft()
    else:
        deck.append(deck.popleft())
    i+=1

print(deck.popleft())

