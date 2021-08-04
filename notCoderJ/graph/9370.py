'''
    풀이 요약
        출발지점 1부터 주어진 도착지점까지 g, h를 거쳐서 가는 경로는 다음 2가지로 나눌 수 있습니다.
            1) 1 -> g -> h -> dest
            2) 1 -> h -> g -> dest
        따라서, 1, g, h를 각각 출발점으로 하여 다익스트라를 수행한 후 도착 지점까지 구간별 최단 거리의 합을 구합니다.
        최종 도착 지점들(dest)을 순회하며 앞서 구한 구간별 최단 거리의 합 중 최솟값과 1 -> dest로의 최단 거리가 일치한다면
        해당 도착 지점을 유효 도착 지점(valid)에 넣어줍니다.
'''
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def execTest():
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    dest = [int(input()) for _ in range(t)]

    def dijkstra(start, dest):
        dist = [INF for i in range(n + 1)]
        dist[start] = 0
        hq = [(0, start)]
        
        while hq:
            d, v = heapq.heappop(hq)
            if d > dist[v]: continue
            
            for nv, w in graph[v]:
                next = d + w
                if next < dist[nv]:
                    dist[nv] = next
                    hq.append((next, nv))
        return {v: dist[v] for v in dest}
    
    path = dijkstra(s, dest + [g, h])
    path1 = dijkstra(g, dest + [h])
    path2 = dijkstra(h, dest + [g])

    shortest = lambda x: min(path[g] + path1[h] + path2[x], path[h] + path2[g] + path1[x])
    valid = []
    for v in dest:
        if shortest(v) == path[v]:
            valid.append(v)

    return sorted(valid)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(*execTest())
