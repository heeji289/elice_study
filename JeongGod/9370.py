import sys, heapq
input = sys.stdin.readline

tc = int(input())

def dijkstra(start):
    length = [1e9 for i in range(N+1)]
    length[start] = 0
    hq = [(start, 0)]
    while hq:
        cur, w = heapq.heappop(hq)

        if w > length[cur]:
            continue
        for next, next_w in graph[cur]:
            nw = next_w + w
            if length[next] > nw:

                length[next] = nw
                heapq.heappush(hq, (next, nw))
    return length

for _ in range(tc):
    flag = False
    N, V, CN = map(int, input().split())
    S, g, h = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(V):
        v1, v2, w = map(int, input().split())
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    candidates = [int(input()) for _ in range(CN)]
    
    # 출발지로부터 g, h로의 거리를 계산한다.
    start_len = dijkstra(S)

    # g, h로 다익스트라로 거리를 계산한다.
    g_len = dijkstra(g)
    h_len = dijkstra(h)
    result = []

    # 후보들과의 거리를 비교한다.
    for cand in candidates:
        if start_len[g] + g_len[h] + h_len[cand] == start_len[cand] or start_len[h] + h_len[g] + g_len[cand] == start_len[cand]:
            result.append(cand)

    print(*sorted(result))

'''
import sys, math, heapq
input = sys.stdin.readline

tc = int(input())

def dijkstra(start):
    length = [math.inf for i in range(N+1)]
    length[start] = 0
    hq = [(start, 0)]
    while hq:
        cur, w = heapq.heappop(hq)

        if w > length[cur]:
            continue
        for next, next_w in graph[cur]:
            nw = next_w + w
            if length[next] > nw:

                length[next] = nw
                heapq.heappush(hq, (next, nw))
    return length

for _ in range(tc):
    flag = False
    N, V, CN = map(int, input().split())
    S, g, h = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(V):
        v1, v2, w = map(int, input().split())
        if (v1 == g and v2 == h) or (v1 == h and v2 == g):
            graph[v1].append((v2,w-0.1))
            graph[v2].append((v1,w-0.1))
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    candidates = [int(input()) for _ in range(CN)]

    start_len = dijkstra(S)

    result = []

    # 후보들과의 거리를 비교한다.
    for cand in candidates:
        if start_len[cand] != math.inf and type(start_len[cand]) is float:
            result.append(cand)

    print(*sorted(result))
'''    
