'''
    풀이 요약
        처음에는 저번 벽을 1번 부술 수 있는 상황에서 최단 거리를 구하는 문제와 비슷한 유형이라고 생각했습니다.
        그래서 저번과 동일하게 bfs를 수행하며 벽을 부수지 않은 맵과 부순 맵 2개의 맵을 그려나가는 방향으로 로직을 구상했습니다.
        하지만, 이번 문제의 경우 최단 거리를 구하는 것이 아닌 최소 벽을 부순 횟수를 구하는 문제이기 때문에 도착 지점에
        돌아가더라도 벽을 최소한으로 부수면 되므로 벽을 부순 횟수의 최소값을 기록하는 맵을 그리는 로직으로 구현했습니다.
        
        1. deque을 이용한 bfs 풀이(첫 번째 풀이한 방법)
            무한값(INF)으로 초기화한 맵을 하나 생성한 후
            1) 각 지점에서 상하좌우의 좌표가 범위 내에 있고
            2) 해당 좌표에서의 이전 부순 횟수가 현재 부순 횟수보다 큰 경우
                그 지점의 부순 횟수를 현재 부순 횟수로 갱신해주고 덱에 (현재 부순 횟수, 해당 지점 좌표)를 넣어줍니다.
            위 과정을 덱이 빌 때까지 반복한 후 n, m에서의 부순 횟수를 반환합니다.
            이 방법은 주어진 입력 범위가 작았기 때문에 가능했었지만, 동일한 지점을 여러 번 방문할 수 있기 때문에
            효율성도 좋지 않고 시간 복잡도를 정확히 가늠하기가 어렵다고 생각합니다.
            
        2. heapq를 이용한 bfs 풀이
            deque을 이용한 풀이와 로직은 거의 동일합니다 하지만, heapq을 이용해서 벽을 부순 횟수가 적은 것부터 처리함으로써
            동일한 지점의 중복 방문을 제거하여 효율성 측면에서 훨씬 개선된 방법입니다.
'''
from collections import deque
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

def solution(m, n, maze):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maps = [[INF] * (m + 1) for _ in range(n + 1)]
    maps[1][1] = 0 # 이 부분을 빼먹어서 또 엉뚱하게 한참 고민했습니다...
    hq = [(0, 1, 1)] # break, x, y
    chkRange = lambda x, y: True if 0 < x <= n and 0 < y <= m else False
    
    while hq:
        br, x, y = heapq.heappop(hq)
        if br > maps[x][y]: continue
        if x == n and y == m: return br

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not chkRange(nx, ny): continue
            nbr = br + (1 if maze[nx - 1][ny - 1] == '1' else 0)
            if nbr < maps[nx][ny]:
                maps[nx][ny] = nbr
                heapq.heappush(hq, (nbr, nx, ny))

    return maps[n][m]


# bfs버전
def solution_bfs(m, n, maze):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maps = [[INF] * (m + 1) for _ in range(n + 1)]
    maps[1][1] = 0
    dq = deque([(1, 1, 0)]) # x, y, break
    chkRange = lambda x, y: True if 0 < x <= n and 0 < y <= m else False
    
    while dq:
        x, y, br = dq.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not chkRange(nx, ny): continue
            nbr = br + (1 if maze[nx - 1][ny - 1] == '1' else 0)
            if nbr < maps[nx][ny]:
                maps[nx][ny] = nbr
                dq.append((nx, ny, nbr))

    return maps[n][m]


if __name__ == "__main__":
    m, n = map(int, input().split())
    maze = [input() for _ in range(n)]
    print(solution(m, n, maze))