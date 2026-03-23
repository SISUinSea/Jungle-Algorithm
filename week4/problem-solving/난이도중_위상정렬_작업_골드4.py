# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

"""
1. 위상정렬한다.
2. 각 작업의 종료 시각을 parent의 종료 시각과 더한다.
3. 그 중에서 최댓값을 출력한다.
"""

from collections import defaultdict, deque

task_count = int(input())

graph = defaultdict(list)
# 위상정렬하기
topo_sort_result = [0] * (task_count + 1)
req_times = [0]
indegree = [0] * (task_count + 1)

for i in range(task_count):
    task_data = list(map(int, input().split()))
    req_times.append(task_data[0])

    for parent_node in task_data[2:]:
        graph[parent_node].append(i + 1)
    indegree[i + 1] = len(task_data[2:])

queue = deque()
for i in range(0 + 1, task_count + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    task = queue.popleft()
    # task의 작업시간 더하기
    topo_sort_result[task] += req_times[task]
    for dep_task in graph[task]:
        # task에 의존하고 있는 작업에 task의 작업시간을 더하기
        # task에 의존하고 있는 작업에서 task 제외하기(indegree --)
        indegree[dep_task] -= 1
        ##  indegree == 0 인 경우 queue에 추가하기
        if indegree[dep_task] == 0:
            topo_sort_result[dep_task] = max(topo_sort_result[task], topo_sort_result[dep_task])
            queue.append(dep_task)


print((topo_sort_result))





















'''
풀이 전략

1. indegree== 0 task 들을 queue에 추가
2. time count, time ++ 마다 queue의 task req time --; 0이면 queue에서 제거
3. 해당 task에 의존하고 있던 task.indegree --; 0이면 enque


deque이 최적의 자료구조가 아니다.
linked list가 파이썬에 있나? 아, deque 자체가 linked list 구나!!

'''
# 이전 시도..
# from collections import deque
#
# class Task():
#     def __init__(self, id, req_time, dependent_tasks):
#         self.id = id
#         self.req_time = req_time
#         self.dependent_tasks = set(dependent_tasks)
#
#     def __str__(self):
#         return f'<id:{self.id}, req_time:{self.req_time}, dep_tasks:{self.dependent_tasks}>'
#
#     def __repr__(self):
#         return self.__str__()
#
# # 입력값 처리
# task_count = int(input())
# tasks = []
# for i in range(task_count):
#     task_data = list(map(int, input().split()))
#     req_time = task_data[0]
#     dependent_tasks = task_data[2:]
#     tasks.append(Task(i+1, req_time, dependent_tasks))
#
# # indegree 계산하기 -> dependent_task의 length로 체크 가능함
#
# # indegree가 0인 작업들 enque
# queue = deque()
# for task in tasks:
#     if len(task.dependent_tasks) == 0:
#         queue.append(task)
# time = 0
# # while 로 반복, time 늘려나가기
# while queue:
#     ## time 증가, 할 일 시작
#     time += 1
#     ## queue에 들어있는 값들의 req time --; 0이 되엇다면 queue에서 제거; 해당 task에 의존하고 있던 task.indegree --; 0이면 enque
#     for ongoing_task in queue:
#         ## $ 모든 작업은 1 이상의 시간을 필요로 함. 0인 작업은 없음을 보장할 수 있다.
#         ongoing_task.req_time -= 1
#         if ongoing_task.req_time > 0:
#             continue
#         # req_time == 0인 경우에 수행
#         queue.remove(ongoing_task)
#         for task in tasks:
#             if ongoing_task.id in task.dependent_tasks:
#                 task.dependent_tasks.remove(ongoing_task.id)
#             if len(task.dependent_tasks) == 0:
#                 queue.append(task)
#
#
#
#     ## task가 queue에 없다면 종료
#
# # time 반환
#
# print(time)
#















