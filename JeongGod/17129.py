'''
3000 * 3000
BFS방식으로 풀자.
'''
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

board = [[int(elem) for elem in input().rstrip()] for _ in range(n)]
for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y] == 2:
            start_x, start_y = x,y



dq = deque()
visited = [[-1] * m for _ in range(n)]

def bfs():
    idx = [(0,1), (0,-1), (-1,0), (1,0)]
    dq.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while dq:
        px, py = dq.popleft()

        for dir in idx:
            nx = px+dir[0]
            ny = py+dir[1]
            # 상하좌우 탐색 및, 방문하지 않은 노드, 벽이 아닌경우
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and board[nx][ny] != 1:
                visited[nx][ny] = visited[px][py]+1
                if 3 <= board[nx][ny] <= 5:
                    return visited[nx][ny]
                dq.append((nx, ny))
    return 0
result = bfs()
print(f"TAK\n{result}" if result != 0 else "NIE")
