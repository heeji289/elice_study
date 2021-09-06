# 특정한 최단 경로

"""
[문제]
1번에서 N번으로 가는 최단 거리를 구하는 문제
but, 임의로 주어진 두 정점은 반드시 통과해야 함
한 번 이동했던 정점, 간선으로 이동이 가능

[생각]
O((V+E)logV) => 우선순위 큐를 사용할 때
알고리즘 참고 : https://justkode.kr/algorithm/python-dijkstra

어떻게 강제로 두 정점을 포함시킬 것인가? 
1번부터 모든 정점까지 최단거리,
v1부터 모든 정점까지 최단거리,
v2부터 모든 정점까지 최단거리를 구하고
1 to v1 to v2 to 끝
1 to v2 to v1 to 끝 비교한다.

딕셔너리 안에 딕셔너리 추가 어떻게? 그냥 리스트로 하자..
=> 진성님 defaultdict(dict)
"""
import sys
import heapq

input = sys.stdin.readline

# n=>v 정점의 개수 e 간선의 개수 
v, e = map(int, input().split())
# a, b, c 시작, 도착, 길이 
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c]) # 양방향임

# v1, v2 반드시 거쳐야 하는 번호 
v1, v2 = map(int, input().split())

def dijkstra(graph, start):
    dist = [float('inf')] * (v+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start], start])  # 시작노드 삽입

    while queue:
        cur_dist, start = heapq.heappop(queue)  # 탐색할 노드, 거리 정보

        # 현재 노드와 연결된 노드 정보를 탐색
        for item in graph[start]:
            end, new_dist = item[0], item[1]
            temp_dist = cur_dist + new_dist  # 지금 노드를 거쳤을 때 end노드까지 거리
            if temp_dist < dist[end]:
                # 최솟값 갱신
                dist[end] = temp_dist
                heapq.heappush(queue, [dist[end], end])
    
    return dist

# 시작점, v1, v2부터 끝까지 모든 최단 거리를 구한다.
start_distance = dijkstra(graph, 1)
v1_distance = dijkstra(graph, v1)
v2_distance = dijkstra(graph, v2)

# 1 to v1 to v2 to 끝
answer = start_distance[v1] + v1_distance[v2] + v2_distance[v]
# 1 to v2 to v1 to 끝 비교
answer2 = start_distance[v2] + v2_distance[v1] + v1_distance[v]
ans = min(answer2, answer)

print(ans if ans < float('inf') else -1)

