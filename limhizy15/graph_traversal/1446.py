# 지름길

"""
세준이는 D 길이의 고속도로를 매일 지난다.
근데 지름길이 있다! 일방통행이다!
세준이가 운전해야 하는 거리의 최솟값은?

거리 배열을 갱신하는 방식으로..
"""
import sys

input = sys.stdin.readline
# n=지름길 개수, d=고속도로길이(도착지점)
n, d = map(int, input().split())

# N개 지름길 정보 (시작 위치, 도착 위치, 지름길의 길이)
shortcut = [list(map(int, input().split())) for _ in range(n)]
road = [i for i in range(d+1)]  # 초기 그래프 정보 (0, 1, 2, ..., d)

for node in range(d+1):
    # 현재 node까지의 최단거리는 본인 or 이전노드 + 1 중 하나
    if node != 0: 
        road[node] = min(road[node], road[node-1] + 1)
    for short in shortcut:
        # 현재 지점에서 시작하는 지름길이 있다면
        if short[0] == node:
            start, end, length = short[0], short[1], short[2]
            # 이어진 점까지 지름길 계산
            if end > d: continue  # 예외처리
            # road배열 최솟값 갱신
            road[end] = min(road[end], road[start] + length)

print(road[d])