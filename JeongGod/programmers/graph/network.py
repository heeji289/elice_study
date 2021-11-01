def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0]*n

    for start, com in enumerate(computers):
        for end, val in enumerate(com):
            # 연결되어있고, 자기 자신이 아니라면
            if val == 1 and start != end:
                graph[start].append(end)

    def dfs(node):
        for v in graph[node]:
            if not visited[v]:
                visited[v] = 1
                dfs(v)

    # 컴퓨터를 다 둘러본다.
    for com in range(n):
        if not visited[com]:
            answer += 1
            dfs(com)

    return answer
