'''
N*M의 크기

빈방은 자유롭게 다닐 수 있다. 벽은 부숴야만 이동 가능

무기를 이용해 벽을 부술수 있다.

궁극의 무기를 이용해 벽을 한 번에 다 없애버릴 수 있다.

1,1 -> N,M으로 이동하려면 몇 개의 벽을 부숴야 하나.

100*100이다. -1,+1을 봐서 벽이면 부순다.

---
다익스트라로 벽을 부수지 않은 최단거리만 뽑아서 간다.
'''
import sys, heapq
input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(input().rstrip()) for i in range(m)]
length = [[1e9]*n for i in range(m)]
def dijstra():
    dir = [(0,-1), (0,1), (1,0), (-1,0)]
    hq = [(0, [0,0])]
    length[0][0] = 0
    
    while hq:
        wall_break, [cur_x, cur_y] = heapq.heappop(hq)
        
        # 최단거리가 이미 존재한다면 보지 않아도 된다.
        if length[cur_y][cur_x] < wall_break:
            continue
        
        # 답을 찾았다면
        if cur_x == n-1 and cur_y == m-1:
            return wall_break
        
        # 동서남북으로 봅니다.
        for idx in dir:
            next_x, next_y = cur_x+idx[0], cur_y+idx[1]
            if 0 <= next_x < n and 0 <= next_y < m and board[next_y][next_x] != "-1":
                if board[next_y][next_x] == "0":
                    heapq.heappush(hq, (wall_break, [next_x, next_y]))
                elif board[next_y][next_x] == "1" and length[next_y][next_x] > wall_break+1:
                    heapq.heappush(hq, (wall_break+1, [next_x, next_y]))
                board[next_y][next_x] = "-1"

print(dijstra())