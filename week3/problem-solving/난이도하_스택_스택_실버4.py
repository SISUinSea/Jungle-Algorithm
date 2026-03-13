# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

instruction_count = int(input())
stack = []
for _ in range(instruction_count):
    instruction = input().split()
    if instruction[0] == 'push':
        stack.append(instruction[1])
    elif instruction[0] == 'pop':
        print(-1 if not stack else stack.pop())
    elif instruction[0] == 'size':
        print(len(stack))
    elif instruction[0] == 'empty':
        print(0 if stack else 1)
    elif instruction[0] == 'top':
        print(stack[-1] if stack else -1)
