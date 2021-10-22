import sys


def solution(n, s, a, b, fares):
    """
    모든 정점에서의 최단 거리를 구한다.
    """
    answer = 0
    dist = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
    # 자기 자신으로 돌아오는건 0이다.
    for i in range(n+1):
        dist[i][i] = 0
    for x, y, fare in fares:
        dist[x][y] = fare
        dist[y][x] = fare

    # 각 정점에서 최단거리를 구한다.
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 시작 지점에서 각자 자신의 목적지로 가는 거리를 초기값으로 잡는다.
    answer = dist[s][a] + dist[s][b]
    # 현재 값, (합승해서 가는 거리 + A로 도착하는 거리 + B로 도착하는 거리) 중에 가장 작은 값
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])

    return answer
