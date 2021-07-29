'''
    풀이 요약:
        해당 문제의 풀이는 기존에 그림과 함께 설명해논 풀이가 더 나은 것 같아서 링크로 걸어둡니다.
        https://github.com/notCoderJ/Algorithm-Study/blob/master/Algorithm_Sites/DFS_BFS/travel_route.md
'''

from collections import defaultdict
import heapq


# 새로 짠 코드
def solution(tickets):
    remain = defaultdict(list)
    for s, d in tickets:
        heapq.heappush(remain[s], d)
    
    def dfs(airport):
        if not remain[airport]:
            return [airport]

        path = []
        while remain[airport]:
            path = dfs(heapq.heappop(remain[airport])) + path
        return [airport] + path
        
    return dfs("ICN")


# 기존에 다른 풀이 중 마음에 들었던 코드를 살짝 변경한 코드
def solution(tickets):
    answer = []
    remain = defaultdict(list)
    for s, d in tickets:
        heapq.heappush(remain[s], d)
    
    st = ["ICN"]
    while st:
        start = st[-1]
        if remain[start]:
            st.append(heapq.heappop(remain[start]))
        else:
            answer.append(st.pop())
            
    return answer[::-1]