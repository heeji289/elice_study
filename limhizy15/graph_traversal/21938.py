# 영상처리

"""
[풀이]
1. 입력을 받아 R, G, B값을 더해 보드에 저장한다. 
2. 평균을 낸 다음 임계값과 비교해 0, 1로 이진화
3. visited배열 만들어서 방문하지 않은 노드 체크
4. 보드를 탐색하면서 값이 1인데 방문하지 않은 노드가 있다면 bfs호출하고 answer + 1
5. bfs는 그냥 네 방향 탐색!
"""

import sys
from collections import deque

input = sys.stdin.readline

# n세로, m가로 입력
n, m = map(int, input().split())
# 보드 생성
board = [[0] * m for _ in range(n)]

# n줄 입력 (R,G,B값이 들어옴)
for i in range(n):
    # 한 줄 입력받아서 리스트로 만든다음        
    temp = list(map(int, input().split()))
    # 리스트 인덱스//3으로 배열에 m값을 정해준다.
    for j in range(len(temp)):
        board[i][j//3] += temp[j]

# T입력
t = int(input())

# 이진화해준다.
for i in range(0, n):
    for j in range(0, m):
        temp = board[i][j] // 3
        # 나누기 3하고 T랑 비교해서 1, 0 결정
        if temp >= t:
            board[i][j] = 1
        else:
            board[i][j] = 0

visited = [[False]*m for _ in range(n)]
answer = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    visited[y][x] = True

    while dq:
        cur_y, cur_x = dq.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            if board[ny][nx] != 1 or visited[ny][nx]: continue

            dq.append((ny, nx))
            visited[ny][nx] = True

# bfs
# deque, visited필요 단순히 연결된 요소를 구하는 것
for i in range(n):
    for j in range(m):
        # 보드를 탐색하면서 1이고 아직 방문하지 않은 노드면 bfs호출 (answer + 1)
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            answer += 1


print(answer)