import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

board = [[] for _ in range(n+1)] # 1 ~ N
for _ in range(m):
    ax, ay = map(int, input().split())
    board[ax].append(ay)

dq = deque()
visited = [False for i in range(n+1)]

# 출발도시중에서 연결되어있는 도시들을 덱에 넣고, 방문표시를 한다.
visited[x] = True
dq.append((x,0))

ans = []
# 덱이 빌때까지 반복한다.
while dq:
    n_node, val = dq.popleft()
    if val == k:
        ans.append(n_node)
        continue

    for node in board[n_node]:
        if not visited[node]:
            dq.append((node, val+1))
            visited[node] = True

ans = sorted(ans)
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)