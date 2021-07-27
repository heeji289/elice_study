'''
    풀이 요약
        이 문제는 익은 토마토를 기준으로 안익은 토마토까지의 가장 먼거리를 계산하면 되겠다고 생각했습니다.
        
        먼저 주어진 정보를 입력받으면서 익은 토마토의 좌표를 deque에 넣어두고 안익은 토마토의 갯수를 카운팅합니다.
        그 후 deque이 빌 때까지 다음 과정을 반복 수행했습니다.
            - deque에서 하나씩 꺼내어 상하좌우에 있는 안익은 토마토에 대해 (해당 토마토 좌표, 현재일자 + 1) 값을 다시 deque에 넣어줍니다.
            - deque에 넣어준 토마토는 값을 계산한 day로 바꾸어주어 재방문 하지 않도록 합니다.
            - 안익은 토마토의 갯수를 1 감소시킵니다.
'''
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


day = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ripe = deque([])
unripe = 0
box = []

m, n = map(int, input().split())
for i in range(n):
    box.append([])
    for j, c in enumerate(map(int, input().split())):
        if c == 0:
            unripe += 1
        elif c == 1:
            ripe.append((i, j, 0))
        box[-1].append(c)

while ripe and unripe:
    x, y, d = ripe.popleft()
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if all([nx >= 0, nx < n, ny >= 0, ny < m]) \
            and box[nx][ny] == 0:
                unripe -= 1
                day = d + 1
                box[nx][ny] = day
                ripe.append((nx, ny, day))

print(day) if not unripe else print(-1)