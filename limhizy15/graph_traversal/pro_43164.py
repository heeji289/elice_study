# 여행경로
# 참고 : https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/

"""
[문제]
a에서 b로 가는 티켓 정보가 tickets에 주어진다.
ICN공항에서 출발할 때, 티켓을 모두 소진하는 방문 경로를 구해라

[풀이]
1. tickets를 인접리스트 형태의 그래프로 생성한다.
2. a에서 갈 수 있는 공항을 알파벳 순서로 정렬한다.
3. DFS로 모든 공항을 순회한다.
    1) 스택의 pop을 cur에 저장한다. (처음엔 ICN)
    2) cur이 그래프에 존재하지 않거나, 더 이상 갈 수 없는 티켓이 없으면 path에 저장한다.
    3) 2)가 아니면 cur을 시작공항으로 갈 수 있는 공항 중 가장 앞에 걸 가져와 stack에 저장한다. (알파벳 순서로 하기 위함)
4. path를 출력한다.
"""
from collections import defaultdict

def solution(tickets):
    # tickets을 {시작점: [도착점 ..]}형태의 인접 그래프로 변형
    graph = defaultdict(list)  # 이거 정리하기
    for start, end in tickets:
        graph[start].append(end)
    
    # DFS
    def dfs():
        # 초기값을 스택에 넣는다.
        s = ["ICN"]
        path = []  # 경로를 담을 변수
        
        while s:
            cur = s[-1]  # 스택의 top값
            # cur에서 출발하는 티켓이 없거나,
            # 티켓이 더이상 남아있지 않은 경우
            if cur not in graph or len(graph[cur]) == 0:
                # 경로에 넣어준다. 이 때 팝!
                path.append(s.pop())
            else:
                # 아니면 다음에 탐색할 곳을 스택에 넣어준다.
                s.append(graph[cur].pop(0))
        # 로직 특성상 경로가 거꾸로 삽입되므로 다시 뒤집어준다.
        return path[::-1]
    
    # graph에서 도착 공항을 정렬해준다.
    for item in graph:
        graph[item].sort()
    
    # DFS를 호출한다.
    answer = dfs()
    
    return answer