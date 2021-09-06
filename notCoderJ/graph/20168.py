'''
    풀이 요약
        다익스트라라고 보기엔 최단 거리를 구하는 문제가 아니어서 애매하긴 하지만, 풀이 과정이 유사한 것 같습니다.
        
        도로의 통행료 중 가장 싼 곳을 먼저 탐색하기 위해 최소 힙을 이용했습니다.
        현재 지점에서 이동할 수 있는 다른 지점 중 도로의 통행료를 지불할 수 있는 지점에 대해서
        [max(현재까지 중 가장 비싼 도로의 통행료, 다음 도로의 통행료) / 다음 지점 / 다음 지점으로 이동했을 때 남은 비용]을 힙에 넣어줍니다.
        힙에서 꺼낸 지점이 도착 지점인 경우 해당 지점까지의 통행료 중 큰 값이 현재까지의 통행료(answer)보다 작다면 answer값을 갱신해줍니다.
'''

import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()


def solutions(start, dest, money, graph):
    answer = 1001
    hq = [(0, start, money)]

    while hq:
        c, n, r = heapq.heappop(hq)
        if n == dest:
            answer = min(answer, c)
        
        for v, w in graph[n]:
            rest = r - w
            if rest >= 0:
                heapq.heappush(hq, (max(w, c), v, rest))
        else:
            graph[n] = [] # 방문 처리를 위해 해주었습니다.
        
    print(answer) if answer < 1001 else print(-1)


if __name__ == "__main__":
    N, M, A, B, C = map(int, input().split())
    inter = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        inter[a].append((b, c))
        inter[b].append((a, c))
    
    solutions(A, B, C, inter)