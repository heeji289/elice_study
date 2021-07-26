'''
n*m의 픽셀로 구성
픽셀당, rgb속성값이 존재
rgb의 평균이 t보다 크면 255, 작다면 0
255면 물체로 인식 => 인접해있는 255짜리도 같은 물체로 인식

일단, 모든 것을 물체로 변환
-> 모든 픽셀을 돌면서 물체인 곳을 찾는다.
-> 찾았다면, BFS방식으로 물체인 것들을 0으로 전환
-> 끝이 난다면 물체의 개수 +1
-> 반복
'''
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

board = [[0]*m for _ in range(n)]

for x in range(n):
    rgb = list(map(int, input().split()))
    standard = 0
    while rgb:
        board[x][standard//3] = sum(rgb[:3])/3
        rgb = rgb[3:]
        standard += 3

t = int(input())

# 물체로 만든다.
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] < t:
            board[i][j] = 0

def check(px, py):
    # 보드밖으로 나갔는지 확인
    if px >= 0 and px < n and py >= 0 and py < m:
        # 물체인지 확인
        if board[px][py] != 0:
            return True
    return False

# bfs형식으로 찾는다.
dq = deque()
idx = [(0,1), (0,-1), (1,0), (-1,0)]
ans = 0
for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y] != 0:
            dq.append((x,y))
            board[x][y] = 0
            ans += 1
        while dq:
            px, py = dq.popleft()
            for dir in idx:
                if check(px+dir[0], py+dir[1]):
                    dq.append((px+dir[0], py+dir[1]))
                    board[px+dir[0]][py+dir[1]] = 0
print(ans)
