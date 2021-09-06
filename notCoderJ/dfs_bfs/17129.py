'''
    풀이 요약:
        이동 경로 간 가중치가 1이고 최단 거리를 구하는 문제이므로 bfs를 이용하면 되겠다고 생각했습니다.
        
        1. 주어진 맵 정보를 입력받으며 값이 2인 경우 시작점에 해당하므로 deque의 시작 값으로 넣어줍니다.(이때 deque에는 현재 좌표 x, y와 해당 지점의 값, 현재 지점까지 거리 정보를 넣어줍니다.)
        
        2. deque이 비거나 최단 경로에 있는 음식점을 찾을 때까지 bfs를 반복 수행합니다.
            - 현재 지점에서 상하좌우에 있는 지점 중 주어진 맵을 벗어나지 않고 빈 복도이거나 해당 지점 값이 2보다 큰 경우에 대해서 다음을 수행합니다.
                deque에 해당 지점 좌표와 지점 값, 현재까지 거리 + 1을 추가하고
                해당 지점 값을 1로 변경하여 지나갈 수 없는 지역으로 만들어 줍니다.(방문처리)
'''

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


answer = -1
n, m = map(int, input().split())

dq = deque([])
island = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

for i in range(n):
    island.append([])
    for j, k in enumerate(map(int, input())):
        if k == 2:
            dq.append((i, j, k, 0))
        island[-1].append(k)

while dq:
    x, y, i, d = dq.popleft()
    
    if i > 2:
        answer = d
        break
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m \
            and (island[nx][ny] > 2 or island[nx][ny] == 0):
                dq.append((nx, ny, island[nx][ny], d + 1))
                island[nx][ny] = 1
    
if answer != -1:
    print("TAK")
    print(answer)
else:
    print("NIE")