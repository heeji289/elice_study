'''
익은 것과 익지 않은 것이 존재한다.
익지 않은 것 옆에 익은게 있다면 하루 뒤에 익는다.
다 익을때의 최소 일수를 구하고 싶다.

visited를 안 쓰는 대신, 익은 토마토를 기준으로 하나씩 늘려가면서 board에 저장.
'''

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

dq = deque()
board = []

for x in range(m):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for y, val in enumerate(tmp):
        if val == 1:
            dq.append((x, y))

idx = [(1,0), (-1,0), (0,1), (0,-1)]

def check(x,y):
    if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
        return True
    return False

ans = 0
while dq:
    x,y = dq.popleft()

    for dir in idx:
        nx = x+dir[0]
        ny = y+dir[1]
        if check(nx, ny):
            board[nx][ny] += board[x][y]+1
            ans = max(ans, board[nx][ny])
            dq.append((nx, ny))

for i in board:
    if 0 in i:
        print(-1)
        exit()
# 처음 입력이 다 익어있는 토마토라면 0을 내뱉어야 하지만, 1을 내뱉게 되서 처리했습니다.
print(ans if ans == 0 else ans-1)