'''
    풀이 요약
        지난 알고리즘 강의때 다뤘던 내용이라서 bfs로 접근하여 풀어봤습니다.
        각 지점(x)에서 2 * x, x - 1, x + 1까지 이동하는데 걸린 시간으로 visited 테이블을 갱신하며
        목표 지점(k)까지 걸린 최단 시간을 계산했습니다.
'''
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
LIMIT = 200_001

def solution(n, k):
    dq = deque([(n, 0)])
    # visited = [-1 for _ in range(LIMIT)] # 기존 버전
    diff = abs(n - k)
    visited = [-1 for _ in range(k + diff + 1)] # 최적화 버전

    while dq:
        cur, sec = dq.popleft()
        if cur == k:
            return sec
        
        # 최적화 버전
        mv = (2 * cur, cur - 1, cur + 1)
        if mv[0] <= k + diff and visited[mv[0]] == -1:
            visited[mv[0]] = sec
            dq.append((mv[0], visited[mv[0]]))
        
        if 0 <= mv[1] and visited[mv[1]] == -1:
            visited[mv[1]] = sec + 1
            dq.append((mv[1], visited[mv[1]]))
            
        if mv[2] <= k and visited[mv[2]] == -1:
            visited[mv[2]] = sec + 1
            dq.append((mv[2], visited[mv[2]]))
        
        # 기존 버전
        # for i, pos in enumerate([2 * cur, cur - 1, cur + 1]):
        #     if 0 <= pos < LIMIT and visited[pos] == -1:
        #         visited[pos] = sec + (1 if i > 0 else 0)
        #         dq.append((pos, visited[pos]))


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))