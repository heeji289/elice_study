# 체스판 다시 칠하기

"""
[문제]
주어진 M*N 크기의 보드를 8*8 크기로 잘라서 체스판을 만들려고 한다.
체스판은 검은색과 흰색이 번갈아 칠해져 있다.
8*8 크기로 잘라서 체스판 조건이 만족하도록 색을 바꿔칠할 때, 칠해야하는 칸의 최소 개수는?

[풀이]
1. 전체 체스판 중 8*8 보드를 찾는다. (탐색)
2. 보드가 결정되면
    1) 흰색시작 or 검정시작
    2) 인덱스가 [짝][짝]이면 시작색과 같고 [짝][홀]이면 다르고
            [홀][짝]이면 다르고 [홀][홀]이면 같다.
    3) 인덱스로 조건문을 둬서 흰색시작일 때 칠해야하면 white_cnt에 아니면 black_cnt에 1을 더함
3. 어떤 게 더 작은지 선택하고 최솟값을 갱신

*** 추출한 판의 시작점이 무조건 기준이 되야한다고 생각하고 풀어서 틀렸다.
*** 흰 / 검 둘 다 가능하도록 바꿔서 고쳤다.
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

answer = 65

for i in range(0, n-7):
    for j in range(0, m-7):
        # 판 하나 선택 => 이제 얘를 돌면서 몇개 바꿀 건지 체크
        white_cnt = 0 
        black_cnt = 0
        start_color = board[i][j]
        for y in range(0, 8):
            for x in range(0, 8):
                cur_color = board[i+y][j+x]
                if y % 2 == 0:
                    if x % 2 == 0:
                        # [짝][홀] => 시작색과 같아야
                        # W면 B시작일 경우 바꿔줘야
                        if cur_color == "W":
                            black_cnt += 1
                        else:
                            white_cnt += 1
                    else:
                        # [짝][홀] => 시작색과 달라야
                        if cur_color == "B":
                            black_cnt += 1
                        else:
                            white_cnt += 1
                else:
                    if x % 2 == 0:
                        # [홀][짝]
                        if cur_color == "B":
                            black_cnt += 1
                        else:
                            white_cnt += 1
                    else:
                        # [홀][홀] 
                        if cur_color == "W":
                            black_cnt += 1
                        else:
                            white_cnt += 1
        # 판 하나 카운팅 성공
        temp = min(white_cnt, black_cnt)
        answer = min(temp, answer)

print(answer)
