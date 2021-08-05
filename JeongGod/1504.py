'''
방향성이 없는 그래프
1번 정점 => n번 정점 최단 거리 이동(다익스트라)
임의로 주어진 두 정점은 반드시 통과.

다익스트라는 1 -> n번까지의 최단거리
'''
import sys,heapq,copy, math
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2,w))
    graph[v2].append((v1,w))

M1, M2 = map(int, input().split())

# length 초기화.
def initial(start, val):
    return [math.inf if i != start else val for i in range(N+1)]

def dijkstra(start, weight):
    length = initial(start, weight)
    hq = []
    heapq.heappush(hq, (start, length[start]))
    while hq:
        cur, total_w = heapq.heappop(hq)
        # 현재 저장된 cur까지가 최소라면 볼 필요가 없다.
        if total_w > length[cur]:
            continue

        # cur정점에서 연결된 간선을 파악한다.
        for next, nw in graph[cur]:
            # cur를 거쳐 지나가는게 더 작다면
            if length[next] > total_w + nw:
                length[next] = total_w + nw
                heapq.heappush(hq, (next, total_w+nw))
    return length



# 1에서 모든 경로 출발.
first = dijkstra(1, 0)

# 1 -> M1 -> M2
second_M1 = dijkstra(M1, first[M1])
third_M2 = dijkstra(M2, second_M1[M2])
# 1 -> M2 -> M1
second_M2 = dijkstra(M2, first[M2])
third_M1 = dijkstra(M1, second_M2[M1])

ans = min(third_M1[N], third_M2[N])
print(-1 if ans == math.inf else ans)
