# 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유

"""
1. 딱따구리 위치를 시작점으로 bfs탐색을 함 (visited, dist 배열)
    1) 1로는 갈 수 없음. 방문한 노드는 방문할 수 없음.
    2) 만약 현재 탐색 중인 곳이 3,4,5 중 하나이면 거기가 최단거리이므로 종료
2. answer이 none이 아니면 TAK과 최단거리 출력

*** 원래는 보드 끝까지 다 탐색하고 3,4,5가 있는 위치를 찾았는데
*** 메모리 초과나서 bfs 사이에서 그냥 return함
"""

import sys
from collections import deque

input = sys.stdin.readline

# n 행 세로, m 열 가로 입력
n, m = map(int, input().split())

# 보드 만들고
board = [[0] * m for _ in range(n)]

# 입력받음 (시작위치인 2위치 기억해둠)
# 3, 4, 5 위치 저장해놓기 딕셔너리에 => 제거
for i in range(n):
    temp = input().rstrip()
    for j in range(m):
        if temp[j] == '2':
            start = (i, j)
        board[i][j] = int(temp[j])

# dist, visited 생성 (각 각 거리, 방문여부 저장)
dist = [[-1] * m for _ in range(n)]
visitied = [[False] * m for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 시작위치에서 bfs호출
# 0이면 못지나감
def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    dist[y][x] = 0

    while dq:
        cur_y, cur_x = dq.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            # 범위 벗어나거나 1로 막혀있거나 이미 방문했으면 continue
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            if board[ny][nx] == 1: continue
            if visitied[ny][nx]: continue

            visitied[ny][nx] = True
            dist[ny][nx] = dist[cur_y][cur_x] + 1

            # 현재 위치가 3, 4, 5 중 하나이면 거리를 리턴
            if board[ny][nx] in [3, 4, 5]:
                return dist[ny][nx]

            dq.append((ny, nx))


answer = bfs(start[0], start[1])

if answer is not None:
    print('TAK')
    print(answer)
else:
    print('NIE')