"""
[그리디 - 회의실 배정]

문제 설명:
- 하나의 회의실에 여러 회의를 배정합니다.
- 각 회의는 시작 시간과 종료 시간이 있습니다.
- 최대한 많은 회의를 배정하려고 합니다.

입력:
- meetings: [(시작, 종료), ...] 회의 리스트

출력:
- 배정된 회의 개수

예제:
입력: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
출력: 4개
선택: [(1, 4), (5, 7), (8, 11), (12, 14)]


"""


"""
# [문제명]

- 링크:
- 분류:
- 결과:

## 1. 문제를 내 언어로
- 처음 이해: 회의실에 최대한 많은 회의를 배정해야 한다. 그 때의 회의실 사용 스케쥴을 반환. 
- 다시 읽고 수정:
- 내가 풀어야 하는 질문 1문장:

## 2. 접근 + 정당성
- 처음 접근: 그리디로 접근한다.
- 왜 된다고 생각했나: 가장 많은 회의를 배정하는 결과는, 종료 시각이 가장 이른 회의 + 종료 시각부터 가장 많은 회의를 배정하는 결과로 같은 subproblem으로 분리할 수 있기 때문이다.
- 최종 접근:
- 왜 맞는가: 사실 잘 모르겠다. 두 가지 핵심 아이디어가 있다. 하나는 진짜 핵심이고 나머지는 곁가지다.
    1. 회의실에 가장 많은 회의를 배정하는 방법은.. 가장 빨리 끝나는 회의를 하나 신청하고, 나머지 회의들을 회의실에 가장 많이 배정하면 된다. 즉, 같은 구조의 subproblem으로 쪼갤 수 있다.
    2. 같은 종료 시각을 가진 회의이면서 배정할 수 있는 회의의 경우, 어떤 회의를 배정하든 전체 회의 개수에 영향을 주지 않는다.

## 3. 푸는 도중
            
    
- 
- 

## 4. 설계

### Greedy
- 선택 기준: 주어진 시작 시간보다 시작 시간이 늦은 회의 (그렇지 않은 경우 회의 일정이 겹친다.)
- 정렬 기준: 회의의 종료 시각
- 성립 이유:

### 풀이:
    1. sort meetings, key=finish time, reversed order
    2. 정렬된 회의 일정에서 가능한 시작 시간과 같거나 늦은 회의를 배정한다. 아닌 경우 다음으로 넘어간다.
    3. 회의를 배정할 경우, 가능한 시작 시간을 해당 회의의 종료시각으로 설정한다.
    4. 모든 요소를 순회하며 회의를 배정한다.
### 의사코드
    1. sort meetings, key=finish_time, reversed = True
    2. available_start_time = 0
    3. for meeting in meetings:
            if meeting.start_time < available_start_time: continue
            result.append(meeting)
            available_start_time = meeting.finish_time

## 5. 실수
- 

## 6. 검증 / edge case
- 손검산:
- 반례1:
- 반례2:
- 반례3:

## 7. 교훈
- 

## 8. 백로그
- 
"""

def select_meetings(meetings):
    """
    회의실 배정 (그리디)
    
    Args:
        meetings: [(시작, 종료)] 리스트
    
    Returns:
        (배정된 회의 개수, 선택된 회의 리스트)
    """
    meetings = sorted(meetings, key= lambda x: (x[1], x[0]))
    selected = [meetings[0]]

    for meeting in meetings:
        if selected[-1][1] > meeting[0]: continue
        selected.append(meeting)

    
    return len(selected), selected

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
    count1, selected1 = select_meetings(meetings1)
    print("=== 테스트 케이스 1 ===")
    print(f"전체 회의: {meetings1}")
    print(f"배정된 회의 개수: {count1}개")
    print(f"선택된 회의: {selected1}")
    print()
    
    # 테스트 케이스 2
    meetings2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    count2, selected2 = select_meetings(meetings2)
    print("=== 테스트 케이스 2 ===")
    print(f"전체 회의: {len(meetings2)}개")
    print(f"배정된 회의 개수: {count2}개")
    print(f"선택된 회의: {selected2}")


