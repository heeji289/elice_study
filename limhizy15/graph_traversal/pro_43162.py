# [DFS/BFS] 네트워크

"""
n: 컴퓨터의 개수 computers: 연결정보 => 네트워크 개수는?
computers[i][j] = 1이면 i와 j가 연결되어있다는 뜻

연결된 덩어리의 개수를 구해야함 => bfs로 연결된 묶음 개수 세면될듯
"""
from collections import deque

def solution(n, computers):
    network = 0
    
    # 방문 체크할 배열
    visited = [False] * n
    
    def bfs(start):
        dq = deque([start])
        visited[start] = True
        
        while dq:
            node = dq.popleft()
            
            for i in range(n):
                if visited[i]: continue
                if computers[node][i] != 1: continue # 연결 안됨
                
                dq.append(i)
                visited[i] = True
                
    for i in range(n):
        if visited[i]: continue
        network += 1 # 새로운 네트워크이므로 더하기
        bfs(i)
    
    return network