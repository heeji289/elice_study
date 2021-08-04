'''
N개의 정점, M개의 간선
1 -> dest까지 가야한다.
최대 weight제일 작은 순으로 간다.
    만약 해당 경로의 weight의 합이 수치심보다 크다면
    다음 weight를 본다.

'''

import sys
input = sys.stdin.readline

n, m, start, dest, money = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    v1, v2, m = map(int, input().split())
    graph[v1].append((m, v2))
    graph[v2].append((m, v1))

result = []
ans = 1e9
def dfs(cur, total, max_money, visited):
    global ans
    if total < 0:
        return
    if cur == dest:
        ans = min(max_money, ans)
    for nm, nv in graph[cur]:
        if nv not in visited:
            dfs(nv, total-nm, max(max_money, nm), visited | {nv})

dfs(start, money, 0, {start})
print(ans if ans != 1e9 else -1)