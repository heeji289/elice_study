'''
m*n board
색칠하는 경우
1. 맨 왼쪽 위칸이 흰색인 경우
2. 맨 왼쪽 위칸이 검은색인 경우

1인경우
    - board[0][0] = 1이라면
    board[짝수][홀수] = 0과 다르다면 개수를 늘린다.
    board[홀수][짝수] = 0과 다르다면 개수를 늘린다.
2인 경우는 1로 무조건 바꾼다는 것만 빼면 같다.

'''
import sys, math
input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

ans = math.inf


for row in range(n-7):
    for col in range(m-7):
        for num in range(2):
            if num == 0:
                target = "BW"
            else:
                target = "WB"
            result = 0
            for i in range(row, row+8):
                for j in range(col, col+8):
                    # 행의 짝홀 판단
                    if i%2 == 0: 
                    # 열의 짝홀 판단
                        if j%2 == 1 and board[i][j] != target[0]:
                            result += 1
                        elif j%2 == 0 and board[i][j] != target[1]:
                            result += 1
                    elif i%2 == 1:
                        if j%2 == 1 and board[i][j] != target[1]:
                            result += 1
                        elif j%2 == 0 and board[i][j] != target[0]:
                            result += 1
            ans = min(result, ans)
print(ans)