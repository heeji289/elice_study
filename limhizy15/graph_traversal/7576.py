# 토마토 (S1)

"""
[문제]
익은 토마토 (1)에 인접한 익지 않은 토마토 (0)은 하루가 지나면 익는다.
=> 이 때 대각선 방향으로 인접한 토마토는 영향을 받지 않는다.
초기의 토마토 상태가 주어질 때, 창고에 있는 모든 토마토가 익기까지 걸리는 최소 일수를 구해라

[풀이]
1. 창고에 있는 1을 모두 덱에 넣는다. (시작점)
2. bfs로 상하좌우 네 방향을 탐색한다. (0인 곳만!)
-> 요소 값을 이전 값 + 1로 해서 일수를 계산해준다.
3. 모든 탐색이 끝나면 보드에 0이 남아있는지 확인하고 제일 큰 값에서 -1을 해준다. (로직상 1부터 계산한 값이 나오므로..)
"""
import sys
from collections import deque

input = sys.stdin.readline

# m 가로, n 세로 입력
m, n = map(int, input().split())

board = [[] * m for _ in range(n)]
# 창고정보 입력 (0: 안익음, 1: 익음, -1: 토마토 없음)
for i in range(n):
    board[i] = list(map(int, input().split()))

# 덱을 선언하고 1의 위치를 모두 삽입해준다.
dq = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dq.append((i, j))

# bfs를 호출한다.

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    # 큐가 빌 때까지
    while dq:
        # 제일 앞 요소 pop
        cur_y, cur_x = dq.popleft()
        # 네 방향 탐색
        for idx in range(4):
            ny, nx = cur_y + dy[idx], cur_x + dx[idx]
            # 조건에 맞지 않는 애들 빼기 (범위, 0이 아닌 것들)
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            if board[ny][nx] != 0: continue

            # 값을 이전값 + 1로 갱신
            board[ny][nx] = board[cur_y][cur_x] + 1
            dq.append((ny, nx))

bfs()

answer = 0
flag = False

# 모두 탐색한 후, 보드에 0이 남아있는지 확인
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer = -1
            flag = True
            break
        elif answer < board[i][j]:
            answer = board[i][j] 
    if flag: break

if flag:
    print(answer)
else:
    print(answer - 1)