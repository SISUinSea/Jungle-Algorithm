"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """

    result = []

    graph = {node : [] for node in range(vertices)}

    # 1. 각 vertex의 indegree를 계산한다.
    indegree = {node : 0 for node in range(vertices)}
    for edge in edges:
        src, dest = edge
        indegree[dest] += 1
        graph[src].append(dest)
    # print(indegree, graph)

    # 2. indegree == 0인 vertices를 enque
    queue = deque()
    for key in indegree:
        if indegree[key] == 0:
            queue.append(key)

    # 3. while queue
    while queue:
        ## 4. v = deque
        v = queue.popleft()
        ## 5. add to result
        result.append(v)
        for adj_v in graph[v]:
            ## 6. v가 directing 하고 있던 vertices의 indegree --
            ## 6.1 만약 indegree == 0인 vertex의 경우 enque
            indegree[adj_v] -= 1
            if indegree[adj_v] == 0:
                queue.append(adj_v)

    # 7. if indegree != 0인 vertex가 있다면 사이클이 존재하는 그래프!
    if len(result) != vertices:
        return None

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
