'''
    풀이 요약
        처음에는 경로를 거쳐간다고 하여 플로이드 워셜을 생각했습니다.
        하지만, 노드가 최대 800개라 3중 for문을 돌리면 터질 것이기 때문에 포기하였고
        각각의 경로로 가는 최단 거리를 구해서 합하면 해당 지점을 거쳐가는 최단 거리가 나올 것이라 생각하여
        각 지점에서 다익스트라를 수행 후 경로의 합이 최소인 지점을 선택하는 로직으로 설계하였습니다.
'''

import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

n1, n2 = map(int, input().split())

def dijkstra(s, d1, d2):
    dist = [INF] * (n + 1)
    dist[s] = 0
    hq  = [(0, s)]
    stop = [False, False]
    
    while hq:
        d, v = heapq.heappop(hq)
        if d > dist[v]:
            continue
        if v == d1:
            stop[0] = True
        elif v == d2:
            stop[1] = True
        if all(stop):
            break
        
        for nv, w in graph[v]:
            next = d + w
            if next < dist[nv]:
                dist[nv] = next
                heapq.heappush(hq, (next, nv)) # 정규님 도움으로 발견한 버그를 수정했습니다!!

    return (dist[d1], dist[d2])
        
isInvalid = lambda x, y: x == INF and y == INF

p1 = dijkstra(1, n1, n2)
p2 = dijkstra(n1, n2, n)
p3 = dijkstra(n2, n1, n)

if isInvalid(p1[0], p1[1]) or isInvalid(p2[0], INF) or isInvalid(p2[1], p3[1]):
    print(-1)
else:
    path1 = p1[0] + p2[0] + min(p3[1], p2[0] + p2[1]) # 1 -> n1 -> min(n2 -> n, n2 -> n1 -> n)
    path2 = p1[1] + p3[0] + min(p2[1], p3[0] + p3[1]) # 1 -> n2 -> min(n1 -> n, n1 -> n2 -> n)
    print(min(path1, path2))
