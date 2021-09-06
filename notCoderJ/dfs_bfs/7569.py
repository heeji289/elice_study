'''
    풀이 요약
        지난 번 토마토 문제의 3차원 확장판이었기 때문에 간단하게 풀이했습니다.
        앞뒤 고려사항이 추가된 것 외엔 지난 번 토마토와 동일하기 때문에 풀이 과정은 지난번과 같습니다.
        
        먼저 주어진 정보를 입력받으면서 익은 토마토의 좌표를 deque에 넣어두고 안익은 토마토의 갯수를 카운팅합니다.
        그 후 deque이 빌 때까지 다음 과정을 반복 수행했습니다.
            - deque에서 하나씩 꺼내어 상하좌우, 앞뒤에 있는 안익은 토마토에 대해 (해당 토마토 좌표, 현재일자 + 1) 값을 다시 deque에 넣어줍니다.
            - deque에 넣어준 토마토는 값을 계산한 days로 바꾸어주어 재방문 하지 않도록 합니다.
            - 안익은 토마토의 갯수를 1 감소시킵니다.
'''

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


days = 0
dq = deque([])
unripe = 0
m, n, h = map(int, input().split())
boxes = []
for x in range(h):
    boxes.append([])
    for y in range(n):
        boxes[-1].append([])
        for z, v in enumerate(input().split()):
            if v == '0':
                unripe += 1
            elif v == '1':
                dq.append((x, y, z, 0))
            boxes[-1][-1].append(v)
            
directions = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)] # 위 아래 왼쪽 오른쪽 앞 뒤
chkDir = lambda x, y, z: True if 0 <= x < h and 0 <= y < n and 0 <= z < m else False # 방향 체크

while dq and unripe:
    x, y, z, d = dq.popleft()
    
    for dx, dy, dz in directions:
        nx, ny, nz = x + dx, y + dy, z + dz
        if chkDir(nx, ny, nz) and boxes[nx][ny][nz] == '0':
            unripe -= 1
            days = d + 1
            boxes[nx][ny][nz] = days
            dq.append((nx, ny, nz, days))

print(days) if not unripe else print(-1)