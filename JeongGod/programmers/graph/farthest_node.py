from collections import deque


def solution(n, edge):
    # BFS로 가장 멀리 떨어진 친구 구하자.
    answer = 0
    graph = [[] for i in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    dq = deque([(1, 0)])
    visited = [0] * (n+1)
    visited[1] = 1
    max_cnt = 0
    while dq:
        cur_v, cnt = dq.popleft()

        if cnt > max_cnt:
            max_cnt = cnt
            answer = 1
        elif cnt == max_cnt:
            answer += 1

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                dq.append((next_v, cnt+1))
                visited[next_v] = 1
    return answer
