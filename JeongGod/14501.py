import sys
input = sys.stdin.readline



n = int(input())
_list = []
for _ in range(n):
    data = tuple(map(int, input().split()))
    _list.append(data)

ans = 0

def dfs(start, cur):
    global ans
    if start > n:
        return
    ans = max(ans, cur)

    for i in range(start,n):
        dfs(i+_list[i][0], cur+_list[i][1])

dfs(0, 0)
print(ans)
