'''
    풀이요약
        합집합 연산과 같은 집합에 속해있는 지 확인하는 것으로 보아 서로소 집합 알고리즘이라는 것을 알았습니다.
        그래서 주어진 합집합 연산에 대해서는 a, b를 합집합 연산해주었고 같은 집합에 속해있는지 확인하는 것은
        두 노드의 루트 노드를 검색해서 사이클이 발생하는지 여부를 확인하여 판별했습니다.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000001)


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_root(a):
    if a != parent[a]:
        parent[a] = find_root(parent[a])
    return parent[a]

def union_set(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    
    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a

isSameSet = lambda a, b: find_root(a) == find_root(b)

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_set(a, b)
    else:
        print("YES") if isSameSet(a, b) else print("NO")