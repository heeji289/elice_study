import sys
from collections import deque
input = sys.stdin.readline

N, M, H = map(int, input().split())
# 3차원 배열을 만들고, 상하좌우 위아래를 보면서 돌아가자.

board = [[] for i in range(H)]
dq = deque()

for h in range(H):
    for y in range(M):
        tmp = list(map(int, input().split()))
        # 익은 토마토를 덱에 넣는다.
        for x in range(len(tmp)):
            if tmp[x] == 1:
                dq.append((h, x, y))
        
        board[h].append(tmp)

# h,x,y
dir = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

def check(nh, nx, ny):
    # 보드밖으로 나갔는지 판단
    if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and board[nh][ny][nx] == 0:
        return True
    return False

h,x,y = 0,0,0
while dq:
    h, x, y = dq.popleft()

    for idx in dir:
        nh = h+idx[0]
        nx = x+idx[1]
        ny = y+idx[2]
        if check(nh, nx, ny):
            dq.append((nh, nx, ny))
            board[nh][ny][nx] = board[h][y][x] + 1

def zero_check():
    for h in board:
        for y in h:
            if 0 in y:
                return False
    return True
print(board[h][y][x]-1 if zero_check() else -1)

