def solution(n, results):
    """
    정확하게 순위가 매겨져있다는 것은 모든 선수와 경기를 했다는 뜻.
    플로이드 워샬 알고리즘 이용
    => 플로이드 워샬알고리즘은 각 정점에서의 최단거리를 구하는 것이 목표이다.
    "여기서는 각 정점들이 연결이 되어있는가?"에 대한 것이 목표이기 때문에 변형해서 사용한다.
    """
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i, j in results:
        graph[i][j] = 1

    # k를 거쳐서
    # graph[i][j] = i선수와 j선수가 붙었으면 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] + graph[k][j] == 2:
                    graph[i][j] = 1

    answer = 0
    for j in range(1, n+1):
        # 내가 이긴 사람의 수
        tmp = sum(graph[j])
        for i in range(1, n+1):
            # 내가 진 사람의 수
            tmp += graph[i][j]
        if tmp == n-1:
            answer += 1
    return answer
