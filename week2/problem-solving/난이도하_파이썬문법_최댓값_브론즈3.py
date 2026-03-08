# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

"""
1. 무엇을 구하나?
- 최댓값, 그 값의 index

2. 입력 / 출력
- 입력: 9개의 자연수
- 출력: 최댓값, 그 값의 index

3. 핵심 제약
- 자연수는 100보다 작다.
- 문제를 풀고 난 뒤..(인덱스가 아니라 몇 번째 수인지를 구해야 했다.)

4. 예제 설명
- 리스트를 순회하며 각 요소가 최댓값이면 최댓값과 index를 업데이트한다.

5. 한 줄 요약
- 결국 이 문제는 최댓값을 찾는 문제다.

6. 접근
-

7. 구현 시작 전 체크
- [x] 문제를 제대로 이해했다
- [x] 예제를 설명할 수 있다
- [x] 왜 이 접근인지 설명할 수 있다
"""
nums = []
for _ in range(9):
    nums.append(int(input()))
max_num = nums[0]
max_index = 0
for i in range(1, len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]
        max_index = i
print(max_num)
print(max_index+1)

