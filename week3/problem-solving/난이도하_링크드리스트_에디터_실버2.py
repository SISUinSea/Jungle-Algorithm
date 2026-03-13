# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406


class Node:
    def __init__(self, char):
        self.char = char
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node('head')
        self.current = self.head

    def add_node(self, data):
        new_node = Node(data)

        new_node.next = self.current.next
        new_node.prev = self.current

        if self.current.next is not None:
            self.current.next.prev = new_node
        self.current.next = new_node

        self.current = new_node
    
    
    def delete_node(self):
        if self.current.char == 'head':
            return
        current = self.current
        next = self.current.next
        prev = self.current.prev
        # move current to left
        self.current = self.current.prev


        # 연결 해제
        if next is not None:
            next.prev = current.prev
            prev.next = next
        else:
            prev.next = None
        # 메모리 해제?


    def print(self):
        target = self.head.next
        while target is not None:
            print(target.char, end="")
            target = target.next
        print()
    

    def move_left(self):
        if self.current.char == 'head': # header node라면
            return
        self.current = self.current.prev

    def move_right(self):
        if self.current.next is None:
            return
        self.current = self.current.next


s = input()


linked_list = LinkedList()
for c in s:
    linked_list.add_node(c)

instruction_count = int(input())
for _ in range(instruction_count):
    instruction = input().split()
    if instruction[0] == "L":
        linked_list.move_left()
    elif instruction[0] == "D":
        linked_list.move_right()
    elif instruction[0] == "B":
        linked_list.delete_node()
    elif instruction[0] == "P":
        linked_list.add_node(instruction[1])

linked_list.print()