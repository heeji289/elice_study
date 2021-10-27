n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# return 4

# n = 4
# costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
# return 9

def solution(n, costs):
    # 최소비용 순으로 정렬
    costs = sorted(costs, key=lambda x:x[2])
    
    mst = [] # 최소신장트리
    parents = [0] # 부모노드

    for i in range(1, n+1):
        parents.append(i) # 처음에는 자기 자신 = 부모 노드

    def find(u):
        if u != parents[u]:
            parents[u] = find(parents[u])
        return parents[u]
    
    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        parents[root2] = root1 # 초기 설정

    mst_cost = 0 # 가중치 합계
    edges = 0 # 간선 개수

    while True:
        if edges == n - 1: # 섬의 개수보다 간선의 개수는 1개 적을 것
            break
        u, v, w = costs.pop(0)
        if find(u) != find(v): # 서로 다른 집합이라면
            union(u, v)
            mst.append((u, v))
            mst_cost += w
            edges += 1


    return mst_cost

# def solution(n, costs):
#     graph = [[] for _ in range(n+1)]

#     for i in range(len(costs)):
#         # 양방향 그래프
#         # (해당 섬에 연결될 다른 섬, 건설 비용)
#         graph[costs[i][0]].append((costs[i][1], costs[i][2]))
#         graph[costs[i][1]].append((costs[i][0], costs[i][2]))

#     build_costs = [INF] * (n + 1)

#     def dijkstra(graph):
#         #초기화
#         q = []
#         heapq.heappush(q, (0, 0)) # 시작할 섬 번호, 자기 자신
#         build_costs[0] = 0 # 시작 지점의 건설 비용(시작 지점은 이미 도착했으니 다리 건설 비용은 0)
        
#         while q:
#             curr_cost, curr_island = heapq.heappop(q) # 현재 섬, 건설 비용 가져오기
#             if build_costs[curr_island] < curr_cost: # 현재까지의 건설 비용이 기존 비용보다 많이 든다면 스킵
#                 continue

#             for next_island, next_cost in graph[curr_island]: 
#                 build_cost = curr_cost + next_cost # 현재까지의 건설 비용 + 다음 섬 건설 비용

#                 if build_cost < build_costs[next_island]: # 다음 섬까지의 기존 건설 비용보다 적다면
#                     build_costs[next_island] = build_cost # 건설 비용 업데이트
#                     heapq.heappush(q, (next_cost, next_island)) # 다음 비용, 다음 섬 푸시


#         return 
    
#     dijkstra(graph)

#     return sum(build_costs[:n-1])


print(solution(n, costs))
