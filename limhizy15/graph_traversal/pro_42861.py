# 그리디 섬 연결하기

"""
연결가능한 조합을 모두 구하고 거리의 최소를 구할까?
최단거리 문제 아닌가?

크루스칼 알고리즘 참고 : https://chanhuiseok.github.io/posts/algo-33/
"""

def solution(n, costs):    
    answer = 0
    
    # 원소가 속한 집합 찾는다
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    # 두 원소가 속한 집합을 합친다
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        
        if a < b: 
            parent[b] = a
        else:
            parent[a] = b
    
    # 부모 테이블 생성
    parent = [i for i in range(n)]

    # 가중치 순 정렬
    costs = sorted(costs, key=lambda x: x[2])
    
    for edge in costs:
        # print(parent)
        a, b, cost = edge
        # 사이클 여부 확인후, 아니면 union!
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer