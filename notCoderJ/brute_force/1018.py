'''
    풀이 요약:
        체스판의 대각선을 기준으로 짝수는 짝수끼리 홀수는 홀수끼리 같으면서
        서로 반대의 색을 지닌다는 것을 이용해야겠다고 생각했습니다.
        
        짝수 대각선 : x, y인덱스의 합이 짝수 / 홀수 대각선 : x, y인덱스의 합이 홀수
        1. 주어진 2차원 보드의 인덱스를 하나씩 탐색하며
            해당 인덱스에서 8*8 크기 범위 내에서 짝수와 홀수 대각선의 각 White, Black수를 계산합니다.
        2. 1번에서 계산한 짝수, 홀수 대각선에서의 각 White, Black 수에서 둘 중 작은 White와 Black의 수를 선택해 더해줍니다.
        3. 주어진 보드의 범위 내에서 1, 2번 과정을 모두 수행한 후 가장 작은 값을 출력합니다.
'''

import sys

input = lambda: sys.stdin.readline().rstrip()


answer = float("inf")
n, m = map(int, input().split())
board = [input() for _ in range(n)]

def paintCnt(i, j):
    odd = [0, 0] # (W, B)
    even = [0, 0]
    
    for x in range(i, i + 8):
        for y in range(j, j + 8):
            if (x + y) & 1:
                odd[1 if board[x][y] == 'B' else 0] += 1
            else:
                even[1 if board[x][y] == 'B' else 0] += 1

    return sum(map(min, zip(odd, even)))

for i in range(n - 7):
    for j in range(m - 7):
        answer = min(answer, paintCnt(i, j))
        
print(answer)