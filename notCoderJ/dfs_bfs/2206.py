'''
    풀이 요약
        허허... 쉽게 생각하고 접근했다가 피봤네요...
        벽 부순 경우랑 안 부순 경우를 한 맵 안에서 처리하려고 끝없이 시도하다가... 결국 포기하고
        구글에서 힌트를 얻어 맵 두개로 분할해서 겨우 통과헀네요 ㅎㅎ
        
        일단 로직은 벽을 부순 맵이랑 안 부순 맵을 두개 만들어놓고
        방문하지 않은 경로(통로이거나 벽이면 부순적 없는 경우)에 대해 탐색하면서
        벽을 부순 경우는 벽을 부순 맵에 현재까지 이동 거리를 표기하고
        벽을 부수지 않은 경우는 부수지 않은 맵에 이동 거리를 표기하며 bfs를 수행합니다.
        두 경우 중 n, m의 위치에서 작은 값을 출력합니다.(단, 둘 중 하나가 0일 경우는 0이 아닌 값을, 둘 다 0인 경우는 -1을 출력합니다.)

'''

from collections import deque
import copy
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


n, m = map(int, input().split())

maze = [[] for _ in range(2)] # [0][][] : 벽 안부순 맵 / [1][][] : 벽 부순 맵
for _ in range(n):
    maze[0].append(list(map(int, input())))
maze[1] = copy.deepcopy(maze[0])
maze[0][0][0], maze[1][0][0] = 1, 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dq = deque([(0, 0, 0)]) # (x, y, break)
chkDir = lambda x, y: True if 0 <= x < n and 0 <= y < m else False

while dq:
    x, y, br = dq.popleft()
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 범위 내에 있고 아직 방문하지 않았으며 통로이거나 벽일 경우 부순적 없는 경우
        if chkDir(nx, ny) and (maze[br][nx][ny] == 0 or maze[br][nx][ny] == 1 and br == 0): 
            cur = maze[br][nx][ny] or br
            maze[cur][nx][ny] = maze[br][x][y] + 1
            dq.append((nx, ny, cur))

answer = list(filter(lambda x: x != 0, [maze[0][n - 1][m - 1], maze[1][n - 1][m - 1]]))
print(min(answer + [INF])) if answer else print(-1)