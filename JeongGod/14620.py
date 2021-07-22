'''
1. sum_board로 미리 덧셈을 해놓은 보드를 만든다.
2. 재귀함수를 돌리면서 진행합니다.
'''
import sys, math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
board = [list(map(int ,input().split())) for i in range(n)]

# 미리 덧셈을 진행해놓는다.
sum_board = [[0 for _ in range(n)] for _ in range(n)]

# 좌, 우, 상, 하, 제자리
dir = [(-1,0), (1,0), (0,1), (0,-1), (0,0)]
for i in range(1,n-1):
    for j in range(1,n-1):
        for idx in dir:
            sum_board[i][j] += board[i-idx[0]][j-idx[1]]

ans = math.inf

# 내가 진행할 수 있는 곳인지 판단하는 곳.
def check(x, y, visited):
    for idx in dir:
        if (x-idx[0], y-idx[1]) in visited:
            return False
    return True

def dfs(cnt, val, visited):
    global ans
    # sum_board는 1~n-2범위가 이루어져있기에 n-1이상을 볼 필요가 없다.
    if cnt == 3:
        print(val)
        ans = min(ans, val)
        return

    for i in range(1,n-1):
        for j in range(1, n-1):
            tmp = []
            # 방문한 적이 없다면
            if check(i, j, visited):
                # 지금 현재 좌표부터 상하좌우, 제자리인 좌표를 집어넣는다.
                for idx in dir:
                    tmp.append((i-idx[0], j-idx[1]))
                dfs(cnt+1, val+sum_board[i][j], visited + tmp)
dfs(0,0,[])
print(ans)