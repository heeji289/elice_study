# MST => 최소 신장 트리

# 1. 크루스칼 알고리즘
"""
크루스칼 알고리즘은 Union-Find를 이용해 진행합니다.
1. 먼저 weight값순으로 정렬합니다.
2. (u, v, weight)를 뽑아 u, v를 하나의 트리로 만듭니다.
3. 이 때, union-find 알고리즘을 이용하여 하나의 트리로 합치는 과정을 진행합니다.
4. 그렇게 모든 간선을 다 돕니다.
"""
import heapq


def solution(n, costs):
    tree = list(range(n))
    rank = [1] * n

    def union(parent, child):
        # 가장 부모를 찾음
        a = find(parent)
        b = find(child)

        # 부모가 같다면, 이미 같은 트리
        if a == b:
            return False

        if rank[a] > rank[b]:
            tree[b] = a
        elif rank[a] == rank[b]:
            tree[b] = a
            rank[a] += 1
        else:
            tree[a] = b
        return True

    def find(node):
        if node == tree[node]:
            return node
        tree[node] = find(tree[node])
        return tree[node]

    # weight순으로 정렬함 (pop을 쓰기 위해 역순으로 정렬)
    costs = sorted(costs, key=lambda x: x[2], reverse=True)
    answer = 0
    while costs:
        u, v, w = costs.pop()
        if union(u, v):
            # u, v를 합칠 수 있다면 weight값을 더 함
            answer += w
    return answer


# Prim 알고리즘
"""
1. 다익스트라랑 비슷한 느낌입니다. 먼저 그래프를 만듭니다.
2. 시작 정점 하나를 선택해 heapq에 넣습니다.
3. heapq에서 가장 작은 weight를 가진 정점 하나를 꺼냅니다.
4. 해당 정점을 방문하지 않았다면 트리로 이어줍니다.
5. 그리고 해당 정점에서 이어진 정점들을 살펴봅니다.
6. 만약, 방문하지 않은 정점이라면, heapq에 넣습니다. heapq는 weight순으로 정렬되게 넣습니다.
7. 3번을 반복합니다.
"""


def solution(n, costs):
    graph = [[] for _ in range(n)]
    for u, v, w in costs:
        graph[u].append((v, w))
        graph[v].append((u, w))

    hq = [(0, 0)]
    visited = [0] * n
    answer = 0
    while hq:
        w, cur = heapq.heappop(hq)
        if visited[cur]:
            continue
        answer += w
        visited[cur] = 1
        for next_n, nw in graph[cur]:
            if not visited[next_n]:
                heapq.heappush(hq, (nw, next_n))
    return answer
