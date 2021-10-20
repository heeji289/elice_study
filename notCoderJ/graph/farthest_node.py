'''
  풀이요약
    1. 주어진 간선으로 graph를 생성합니다.
    2. 1번 노드부터 시작하여 bfs를 이용해 graph를 순회하며 각 노드까지의 거리를 구합니다.
    3. 최대 거리인 노드들의 숫자를 반환합니다.
'''

from collections import deque

def solution(n, edge):
    dist = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    dq = deque([1])
    while dq:
        current = dq.popleft()
        for node in graph[current]:
            if not dist[node]:
                dist[node] = dist[current] + 1
                dq.append(node)

    return len([d for d in dist[2:] if d == max(dist)])