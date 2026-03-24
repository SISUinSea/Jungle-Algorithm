# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639



"""
# 풀이 전략
1. 전위순회 결과값을 가지고 트리를 만든다.
2. 트리를 후위순회한 값을 출력한다.


# 1에 대한 상세 전략
1. 첫 입력값은 root이다.
2. 현재 node보다 작다면 left에 연결한다. left가 이미 연결되어 있다면 left에게 연결 책임을 넘긴다.
3. 현재 node 보다 크다면 위로 올린다. root인 경우는 바로 right로 연결한다.
    3.1 위로 올려서 해당 node 보다 큰 node를 만났다면, 그 큰 node 보다는 작은 것이다. 그 큰 node의 left의 right로 연결한다.


# 트리는 어떻게 만들까? 트리 객체? 아니면 그냥 배열(defaultdict?)



---------

채강이가 트리 노드를 만들어서 풀면 시간초과가 난다고 해서 다른 풀이로 접근하는 중이다...

규칙은 발견했다. 전위순회를 바로 후위순회로 바꾸는 규칙.. 하지만 말로 풀어서 설명하기가 어렵다.


규칙을 함수로 부르고 다음과 같은 함수를 재귀로 부른다.

def f(
        i, # i th node를 루트로 하는 트리에서
        m, # m보다 크고
        M  # M보다는 작은 노드들을 후위순회로 출력하라
    )
    if arr index out of range: return i
    if arr[i] > M: return i

    next_ptr = f(i + 1, 0, M)
    next_ptr = f(next_ptr, arr[i], M)
    print(arr[i], end=" ")
    return next_ptr
"""
import sys
sys.setrecursionlimit(10**5)
CONST_MAX = 10**6 + 1

def f(
        i, m, M
):
    global arr
    if i >= len(arr): return i
    if arr[i] > M: return i

    std = arr[i]

    next_index = f(i + 1, 0, arr[i])
    next_index = f(next_index, arr[i], M)
    print(arr[i], end=' ')
    return next_index

arr = list(map(int, sys.stdin.buffer.read().split()))

index = f(0, 0, CONST_MAX)
f(index, arr[0], CONST_MAX)



# 이전 풀이 남겨둔 것...
# class Node:
#
#     def __init__(self, val, parent=None):
#         self.parent = parent
#         self.left = None
#         self.right = None
#         self.val = val
#
#     def __str__(self):
#         return f"Node(val={self.val}, left={self.left}, right={self.right})"
#
#     def __repr__(self):
#         return self.__str__()
#
#
# def add_node_into_tree(root:Node, target:Node, new_val:int):
#     if target.val > new_val:
#         while target.left is not None: # 처음 들어가고 났을 때의 노드보다 큰 값이면 어쩌려고???? 이거 고쳐야 해. 잘못된 로직임.
#             target = target.left
#         target.left = Node(new_val, target)
#     elif target.val < new_val:
#         while target != root and target.val < new_val:
#             target = target.parent
#         if target == root:
#             target.right = Node(new_val, target)
#         else:
#             target.left.right = Node(new_val, target.left)
#
#     return target
#
#
#
#
# def print_postorder(root):
#     pass
#
#
# import sys
#
#
# arr = list(map(int, sys.stdin.buffer.read().split()))
#
# root = Node(arr[0])
# current = root
#
#
#
# for i in range(1, len(arr)):
#     print(arr[i])
#     current = add_node_into_tree(root, current, arr[i])
#
#
# print(root)

