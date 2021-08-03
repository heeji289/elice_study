# 맥주 마시면서 걸어가기

"""
50미터에 한 번씩 맥주를 마셔야 이동 가능. (편의점 가서 구입가능)
그러면 50*20 = 1000만큼의 거리는 이동이 가능하다.

상근집 - 편의점들 - 페스티벌까지 무사히 갈수있는지?
"""
import sys
from collections import deque

input = sys.stdin.readline
INF = 100000

# t 테스트케이스 수 
t = int(input())
for _ in range(t):
    # n 편의점의 개수
    n = int(input())
    # 상근이 집, n개 편의점, 도착 지점 좌표가 주어짐 / 거리=x좌표차이+y좌표차이
    pos = [list(map(int, input().split())) for _ in range(n+2)]

    # 그래프정보 담을 곳
    dist = [[INF] * (n+2) for _ in range(n+2)]

    # 모든 좌표들을 탐색하면서
    # i to j까지 거리가 1000이하이면 dist[i][j] = 1을 삽입해준다.
    for i in range(n+2):
        for j in range(n+2):
            if i == j: continue
            dist_temp = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
            if dist_temp > 1000: continue  # 이동 불가능한 경우 예외처리
            dist[i][j] = 1  # 갈 수 있는 길이므로 표시해줌

    # dist배열을 보면서 모든 정점의 최단거리를 구함 (플로이드~)
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if dist[i][j] < dist[i][k] + dist[k][j]: continue
                dist[i][j] = dist[i][k] + dist[k][j]
    
    if dist[0][n+1] != INF:
        print('happy')
    else:
        print('sad')

