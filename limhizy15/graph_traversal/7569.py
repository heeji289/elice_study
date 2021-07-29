# 토마토
"""
[문제]
1. M * N * H 창고에 토마토가 있다. 
2. 익지 않은 토마토는 익은 토마토의 영향을 받아 익는다. (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
3. 며칠이 지나면 토마토가 다 익는지 구해라.

[풀이]
BFS 탐색할 때 네 방향 + 위, 아래 체크
3차원 배열 입력은 어떻게 받을 것인가?
"""
import sys
from collections import deque

input = sys.stdin.readline

# M: 가로, N: 세로, H: 상자의 수 입력
m, n, h = map(int, input().split())

# 가장 밑의 상자부터 위에까지 토마토 정보 입력
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 보드를 탐색하면서 1인 곳의 좌표를 덱에 저장
dq = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                dq.append((i, j, k))

# 상 하 좌 우 위 아래
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# bfs
def bfs():
    # 덱이 빌 때까지
    while dq:
        # 가장 앞에 있는 요소를 꺼낸다.
        cz, cy, cx = dq.popleft()
        # 6방향을 탐색한다. 2차원기준 상하좌우와 3차원 기준 위아래
        
        for i in range(6):
            nz, ny, nx = cz + dz[i], cy + dy[i], cx + dx[i]
            # 범위 체크
            if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            if board[nz][ny][nx] != 0: continue
            # 보드 값을 +1로 갱신
            board[nz][ny][nx] = board[cz][cy][cx] + 1
            dq.append((nz, ny, nx))

# bfs 탐색
bfs()

answer = 0
flag = False

# 보드를 모두 돌면서 익지 않은 곳이 있는지 체크
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                answer = -1
                flag = True
                break
            elif answer < board[i][j][k]:
                answer = board[i][j][k]
        if flag: break
    if flag: break

# 출력
if flag:
    print(answer)
else:
    print(answer - 1)
