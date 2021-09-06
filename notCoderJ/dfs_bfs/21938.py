'''
    풀이 요약:
        먼저 주어지는 각 픽셀의 RGB 정보를 입력받아 픽셀의 RGB 평균값을 구하고 리스트에 저장합니다.
        1. dfs 풀이
            n * m 픽셀을 하나씩 탐색하며 해당 픽셀의 평균값이 경계값(t)보다 크고 256(방문 처리)이 아닌 값이 존재할 경우 물체의 수를 1 증가시키고 해당 픽셀에서 dfs를 수행합니다.
            
            dfs는 해당 픽셀의 값을 256으로 변경하여 방문 처리한 후 n*m 화면을 벗어나지 않고
            값이 t보다 크거나 같은 방문하지 않은 상하좌우에 있는 픽셀에 대해 dfs를 반복적으로 수행하여 물체를 표시합니다.
            
        2. bfs 풀이
            dfs와 동일한 로직이며 dfs를 수행하는 부분을 bfs로 대체하여 수행합니다.
'''


from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


answer = 0
n, m = map(int, input().split())
avg = lambda x: sum(x) / 3

screen = [[] for _ in range(n)]
for i in range(n):
    line = tuple(map(int, input().split()))
    for j in range(0, 3 * m, 3):
        screen[i].append(avg(line[j:j+3]))
t = int(input())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

# bfs 풀이
def processImg(i, j):
    dq = deque([(i, j)])
    
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m \
                and screen[nx][ny] >= t and screen[nx][ny] < 256:
                screen[nx][ny] = 256
                dq.append((nx, ny))


for i in range(n):
    for j in range(m):
        if screen[i][j] >= t and screen[i][j] < 256:
            answer += 1
            processImg(i, j)

print(answer)


# dfs 풀이
# def processImg(x, y):
#     if screen[x][y] < t or screen[x][y] == 256:
#         return False
    
#     screen[x][y] = 256
    
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             processImg(nx, ny)

#     return True