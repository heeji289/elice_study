import sys, copy
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for i in range(n)]
# 1,1이 들어온다면 바로 끝내게 설정했습니다.
if n == 1 and m == 1:
    print(1)
    exit()

wall_visited = copy.deepcopy(board)

dq = deque([(0, 0, False, 1)])
board[0][0], wall_visited[0][0] = -1, -1
# 0,0 부터 시작한다.
dir = [(0,-1), (0,1), (1,0), (-1,0)]

def check(nx, ny, wall):
    if 0 <= nx < m and 0 <= ny < n:
        # 벽을 뚫은 경우에는 벽의 방문경로로 판단한다.
        if wall:
            if wall_visited[ny][nx] == '0':
                return 2
        # 벽이 아니라면
        elif not wall:
            # 갈 수 있는 공간
            if board[ny][nx] == '0':
                return 1
            # 벽을 만났지만 부수지 않은 경우라면
            elif board[ny][nx] == '1':
                return 2
    return 0

def bfs():
    while dq:
        x, y, wall, ans = dq.popleft()
        for idx in dir:
            nx = x+idx[0]
            ny = y+idx[1]
            if nx == m-1 and ny == n-1:
                ans += 1
                return ans
            way = check(nx, ny, wall)

            if way > 0:
                # 벽을 부수지 않은 경우
                if not wall:
                    board[ny][nx] = '-1'
                    wall_visited[ny][nx] = '-1'
                # 벽을 이미 부쉈던 경우
                else:
                    wall_visited[ny][nx] = '-1'

                # 벽이 아닐 경우에는
                if way == 1:
                    dq.append((nx, ny, wall, ans+1))
                # 벽을 부순 경우거나 이미 부쉈던 경우인데 가능하다면
                elif way == 2:
                    dq.append((nx, ny, True, ans+1))
result = bfs()
print(result if result != None else -1)

