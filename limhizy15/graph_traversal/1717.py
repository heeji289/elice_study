# 집합의 표현

"""
[문제]
0부터 n까지 각각 집합이 있다.
합집합 연산, 두 원소가 같은 집합에 포함되어있는지 확인하는 연산 2개를 구현

[생각]
1반 코치님이 코테에 자주나온다고 했던 유니온 파인드! 근데 어떻게 구현하는지 모름
https://ip99202.github.io/posts/%EC%9C%A0%EB%8B%88%EC%98%A8-%ED%8C%8C%EC%9D%B8%EB%93%9C(Union-Find)/

Union : 두 원소가 주어질 때 이들이 속한 두 집합을 하나로 합침
Find : 어떤 원소 a가 주어질 때 이 원소가 속한 집합을 반환
"""
import sys
sys.setrecursionlimit(10**5)  # 재귀...제한.....
input = sys.stdin.readline

# n 집합의 개수 , m 연산의 개수
n, m = map(int, input().split())

# 부모 테이블을 생성
# 자기 자신을 부모로 설정
parent = [i for i in range(n+1)]

# 루트 노드를 찾는 함수
def find(a):
    if a == parent[a]: return a # 부모가 자기자신일 때 
    parent[a] = find(parent[a]) # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: return # 같은 집합 안에 있음
    if a < b: # 합침 => 같은 부모 노드를 갖도록 함
        parent[b] = a
    else:
        parent[a] = b

# 연산 정보
# 0 a b 합집합 => a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합침
# 1 a b 같은 집합에 포함되어 있는지 확인 => YES or NO 체크
ans = []

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union(a, b)
    else:
        if find(a) == find(b): # 동일한 집합 (동일한 루트 노드)
            ans.append('YES')
        else:
            ans.append('NO')

for item in ans:
    print(item)