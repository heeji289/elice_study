from collections import defaultdict
def solution(tickets):
    # dict사용
    graph = defaultdict(list)
    for key, value in tickets:
        graph[key].append(value)

    for k in graph:
        graph[k].sort()
    
    def dfs(cur, result):
        # 모든 공항을 방문한다면
        if len(result) == len(tickets)+1:
            return result
        
        # 모든 그래프를 방문한다.
        for idx,port in enumerate(graph[cur]):
            graph[cur].remove(port)
            
            # DeepCopy
            tmp_result = result[:]
            tmp_result.append(port)
            
            # 방문한 그래프를 다시 간다.
            a = dfs(port, tmp_result)
            
            if a: return a
            
            # return값이 None값이라면
            # 다시 티켓을 반환한다.
            graph[cur].insert(idx, port)
        
    answer = dfs("ICN", ["ICN"])
    return answer