'''
    풀이요약
        다익스트라나 플로이드 워셜 같은 그래프 알고리즘의 경우 도착 지점까지 경로가
        연결된 상황에서만 풀이해봐서 그런지 경험이 극히 제한적이여서 방향성을 잡기가 어렵네요 ㅎㅎ;
        여러 번 시도했지만 계속 이상한 방향으로 흘러가는 느낌이라 결국 구글의 힘을 빌렸습니다.
        다익스트라와 다이나믹 프로그래밍이 섞여있는 알고리즘입니다.
        
        먼저, 주어진 도로 간 정보를 defaultdict를 이용해서 기록해두고
        최단 거리를 기록할 dist 테이블을 각 지점의 거리로 초기화합니다.
        현재 거리와 이전까지 거리 + 1을 비교하여 현재까지 거리를 최단 경로로 갱신합니다.
        현재 경로에 연결된 지름길이 있을 경우 해당 지름길의 도착 지점에서 거리가 지름길을 이용했을 때
        이득이라면 해당 도착 지점까지 거리를 지름길 거리 + 현재까지 거리 값으로 갱신해줍니다.
'''

from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


n, D = map(int, input().split())
road = defaultdict(list)
for _ in range(n):
    s, e, d = map(int, input().split())
    road[s].append((e, d))
    tmp = road[e] # 도착 지점이 빈리스트일 경우 다익스트라 내부에서 해당 값과 비교 시 새로운 항목이 생성되는 에러 방지용

dist = [i for i in range(D + 1)]

for i in range(D + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)
    for e, w in road[i]:
        eDist = dist[i] + w
        if e <= D and eDist < dist[e]:
            dist[e] = eDist
            
print(dist[D])