# 벽 부수고 이동하기
"""
n * m 맵이 있다. 0은 이동할 수 있는 곳, 1은 이동할 수 없는 곳.
(1, 1) 부터 (N, M)까지 가려는데 최단 경로로 가려한다.
이동 도중 벽을 한개 부술 수 있다.
시작, 도착점은 항상 0이다.

bfs탐색을 한다.
덱에 삽입되는 것은 (y, x, cnt)로 위치와 벽을 부순 횟수를 나타낸다.
visited는 3차원으로 [0]이면 안 부수고 지나간 것 [1]이면 부수고 지나간 것
"""
import sys
from collections import deque

input = sys.stdin.readline

# n, m 입력 세로가로
n, m = map(int, input().split())

# 보드 입력
board = [list(map(int, input().rstrip())) for _ in range(n)]

# 방문 여부 판단 
# [[[0, 1], [0, 1], [0, 1]],
#  [[0, 1], [0, 1], [0, 1]]]
# 벽을 안부수고 방문 & 벽을 부수고 방문 => 방문 체크 겸 거리 계산도
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

# bfs 탐색 세팅
dq = deque()
dq.append((0, 0, 0))  # 시작점과 벽부순 횟수 추가 (0)
visited[0][0][0] = 1  # 안부수고 방문했으니까!
# visited[0][0][1] = 1

# 네 방향
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# bfs 탐색
while dq:
    y, x, cnt = dq.popleft()
    # print(y, x, cnt)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        # 범위를 벗어난 경우
        if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
        # 빈칸이고 아직 방문하지 않은 곳이라면
        if board[ny][nx] == 0 and visited[ny][nx][cnt] == 0:
            visited[ny][nx][cnt] = visited[y][x][cnt] + 1
            dq.append((ny, nx, cnt))
        # 다음칸이 벽이고, 아직 벽을 부수지 않았고, 해당 벽을 부수고 방문한 적이 없으면
        if cnt == 0 and board[ny][nx] == 1 and visited[ny][nx][cnt+1] == 0:
            visited[ny][nx][cnt+1] = visited[y][x][cnt] + 1
            dq.append((ny, nx, cnt+1))  # 벽을 부순 횟수를 갱신해줘야


# bfs 호출
# bfs()

if visited[n-1][m-1][0] != 0 and visited[n-1][m-1][1] != 0:
    print(min(visited[n-1][m-1][0], visited[n-1][m-1][1]))
elif visited[n-1][m-1][0] != 0:
    print(visited[n-1][m-1][0])
elif visited[n-1][m-1][1] != 0:
    print(visited[n-1][m-1][1])
else:
    print(-1)