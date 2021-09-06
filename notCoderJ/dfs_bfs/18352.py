'''
    풀이 요약
        주어진 문제는 방향성 있는 그래프에서 최단거리를 구하는 문제이므로 bfs, 다익스트라 둘다 가능하다고 생각했습니다.
        (bfs가 가능한 이유는 이동간 가중치가 1이기 때문에 가능하다고 생각했습니다.)
        
        다익스트라 풀이
            시작점부터 시작하여 다음 과정을 반복 수행합니다.
            연결된 각 도시들에 대해 해당 도시까지의 거리를 계산하고 현재 거리보다 작은 경우
            해당 도시까지의 거리를 갱신하고 heapq에 (거리, 도시) 값을 추가해줍니다.
            heapq에서 꺼낸 도시 중 거리가 k인 도시는 answer에 추가하고
            k보다 클 경우 더 이상 k보다 짧은 거리는 나오지 않으므로 반복을 종료합니다.
            answer이 비어있으면 -1 존재하면 오름차 정렬 후 각 도시 번호를 출력해줍니다.
        
        bfs풀이
            전반적으로 다익스트라와 비슷한 로직을 띄고 있고 2가지 차이점이 있습니다.
            1. heapq 대신 deque을 사용한다는 점
            2. 해당 지점까지 현재 거리와 다음 거리를 비교하는 것이 아닌 방문 처리 여부를 통해 해당 지점을 탐색한다는 점
'''

import heapq
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


answer = []
n, m, k, x = map(int, input().split())
citys = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    citys[a].append(b)

# 다익스트라를 이용한 풀이
INF = int(1e9)

shortest = [INF] * (n + 1)
shortest[x] = 0
hq = [(0, x)]

while hq:
    dist, cur = heapq.heappop(hq)
    if dist > shortest[cur]:
        continue
    if dist == k:
        answer.append(cur)
    elif dist > k:
        break
    
    for city in citys[cur]:
        next = dist + 1
        if next < shortest[city]:
            shortest[city] = next
            heapq.heappush(hq, (next, city))

print(*sorted(answer), sep='\n') if answer else print(-1)

# bfs를 이용한 풀이
# visited = [False] * (n + 1)
# visited[x] = True
# dq = deque([(x, 0)])

# while dq:
#     cur, dist = dq.popleft()
    
#     for city in citys[cur]:
#         if not visited[city]:
#             next = dist + 1
#             visited[city] = True
#             if next == k:
#                 answer.append(city)
#             elif next > k:
#                 break
#             dq.append((city, next))

