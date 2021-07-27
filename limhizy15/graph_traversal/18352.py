# 특정 거리의 도시 찾기 (S2)

"""
[문제]
1부터 N번까지 도시, M개의 단방향 도로가 존재 (거리는 1)
X도시부터 도달할 수 있는 모든 도시 중에 최단 거리가 K인 도시들의 번호를 찾아라

[생각]
1. 입력으로 받은 도로 정보를 인접리스트로 저장
2. visited 배열을 N만큼 생성
3. bfs로 탐색 
- graph[i]로 연결되어 있는 애들 모두 탐색 (이미 방문한 곳 제외)
- 방문 안한 곳은 덱에 삽입하면서 거리를 이전 +1 해준다. 
=> 이 결과가 K라면 정답 배열에 삽입

[입출력]
N 도시 개수 M 도로 개수 K 거리 X 출발 번호
A, B (A -> B 도로가 존재, 같은 수는 안나옴)

한 줄에 하나씩 오름차순, 존재하지 않으면 -1
"""
import sys
from collections import deque

input = sys.stdin.readline

# n, m, k, x 입력
n, m, k, x = map(int, input().split())

# graph와 visited 배열 생성 + dist배열도
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [-1] * (n + 1)

# 도로 정보 입력받아서 인접리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발도시를 덱에 삽입
dq = deque()
dq.append(x)
visited[x] = True
dist[x] = 0

answer = []

# bfs 탐색
def bfs():
    while dq:
        # 덱에서 꺼내고
        cur = dq.popleft()
        # 얘와 연결된 애들 탐색 (graph[i])
        for i in range(len(graph[cur])):
            next = graph[cur][i]
            if visited[next]: continue
            # 만약 방문 안햇으면 visited해주고 거리를 dist[next] = dist[cur] +1 해준다.
            visited[next] = True
            dist[next] = dist[cur] + 1
            dq.append(next)
            # 이 값이 K면 정답 배열에 삽입
            if dist[next] == k:
                answer.append(next)

# bfs 호출
bfs()

answer.sort()  # 정렬!!!
# 정답 출력
if len(answer) == 0:
    print(-1)
else:
    for item in answer:
        print(item)