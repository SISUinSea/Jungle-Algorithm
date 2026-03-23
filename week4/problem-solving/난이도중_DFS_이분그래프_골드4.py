# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707


"""
될 것 같다.
하지만 확실하게 보장하고 가보자.

일단, 어떤 풀이인가?

1. 위상정렬을 통해서 root를 찾는다.(root가 여러개라면?) -> 수정: 꼭 root가 아니어도 됨.
2. DFS를 통해서 탐색한다. (/ BFS도 될 것 같은데..?) 현재 칸을 0/1로 표시하는 패리티 비트를 만든다. '0'인 칸에서 인접한 칸은 '1'로 설정한다.
3. 탐색한 칸은 visited로 표시한다. 한 번 탐색한 칸은 다시 탐색할 필요 없다.
4. 하나의 가지를 탐색할 동안 0인 정점이 다른 0인 정점과 만나거나, 1인 정점과 1인 정점과 만나면 False.
5. 모든 v를 탐험하는 동안 한 번도 충돌이 발생하지 않았다면 True
**. 어떤 v와 인접한 노드 u가 이미 visited라면, 그 가지는 다시 보지 않아도 괜찮다.

V <= 20,000, E <= 200,000 이어서 DFS = O(VE)인 경우, 시간초과가 나는 것 아닌가 생각했지만...
모든 탐색을 하는 것도 아니고, 알고리즘 시간 복잡도의 상한은 V로 재설정된다(한번 탐험한 정점은 다시 탐험하지 않기 때문에)
그럼 20,000 * 5 = 100,000 정도면 안전하게 통과 가능해보인다.

중요한 점은 DFS 로 탐험할 때 사용하는 가지를 위한 스택과 visited를 분리해야 한다는 점이다.

"""
# todo.  V + 1, V+1+1에 대해서 정확하게 내가 지금 해석하고 있나????????
# V개의 노드를 만들어야 한다. 근데? 1based indexing을 쓰기 때문에 V + 1을 해준다. 그럼 V + 1 + 1은 뭐고, 이걸 했을 때의 예외 상황이 발생할 수 있을 건 뭐지?


# 재귀 방식을 iterative하게 바꿔서 스택을 사용하고 있는데, 각 path를 탐색할 때마다 그 상태를 되돌리고 있나?
k = int(input())
for _ in range(k):
    V, E = map(int, input().split())
    # 인접 리스트를 만든다. 입력값을 받아서 완성한다.
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        src, dst = map(int, input().split())
        adj[src].append(dst)
        adj[dst].append(src)

    visited = [0] * (V + 1)
    crashed = False
    # 탐험하지 않은 모든 V를 탐험한다. 탐험한 V는 visited[v] = 1로 표시한다.
    for i in range(1, V + 1):
        # parity 배열을 -1로 초기화한다.
        parity = [-1] * (V + 1)
        # 시작 정점을 스택에 넣고 스택이 빌 때까지 돌린다.
        stack = [i]
        parity[i] = 0
        while stack:
            # 스택에서 정점을 꺼낸다. 해당 정점은 이미 parity 그룹이 결정되어 있다.(0/1)
            v = stack.pop()
            # 이미 방문한 정점이라면 넘긴다. 아니라면 방문 표시를 한다.
            if visited[v] == 1:
                continue
            visited[v] = 1
            for u in adj[v]:
                # 만약, 인접한 정점의 parity가 설정되어 있고, 부여하려고 하는 패리티와 다른 경우(인접한 정점v와 패리티가 같은 경우) 충돌이 발생한 것이다.
                if parity[u] != -1 and parity[u] == parity[v]:
                    crashed = True
                    break
                # 인접한 정점들에 parity 배열을 사용해서 1/0 을 표시한다.
                # todo. 의심 포인트 -> 이미 패리티를 심은 애들도 덮어쓰게 된다. 근데 그랬을 때 문제가 발생하나? 한다면 어떤 case가 있지?
                # 없어!! 왜냐하면... 이미 충돌나는 케이스는 제외했으니까!!
                if parity[v] == 0:
                    parity[u] = 1
                else:
                    parity[u] = 0
                stack.append(u)

            if crashed:
                break
        if crashed:
            break

    # 모든 정점에 대해서 탐험을 마쳤을 때 충돌이 발생하지 않았다면 이분 그래프이다.
    if crashed:
        print("NO")
    else:
        print("YES")

