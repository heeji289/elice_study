'''
    풀이요약
        먼저, 가능 여부를 확인하는 dist 테이블을 False로 초기화한 후 각 자신의 지점 값을 True로 갱신해줍니다.
        그 다음 플로이드 워셜 알고리즘을 사용해서 지점 간 이동이 가능한지 확인하고 가능하다면 dist 테이블의 값을 True로 갱신해주었습니다.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()


def floyd(n, places):
    dist = [[False] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = True

    manhattan = lambda x1, x2: abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])
    isValid = lambda x, y: True if x or y else False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if not dist[j][k] and \
                isValid(dist[j][i], manhattan(places[j], places[i]) <= 1000) and \
                isValid(dist[i][k], manhattan(places[i], places[k]) <= 1000):
                    dist[j][k], dist[k][j] = True, True

    return dist[0][n - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    places = [tuple(map(int, input().split())) for _ in range(n + 2)]
    print("happy") if floyd(n + 2, places) else print("sad")