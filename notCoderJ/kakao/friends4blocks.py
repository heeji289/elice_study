'''
  풀이요약
    1. remove 함수
      각 블럭을 순회하면서 4개가 동일한 블럭인지 확인하고 동일하면 각 좌표를 집합에 넣습니다.
      집합에 포함된 좌표의 블럭 값을 0으로 변경한 후 집합의 길이(없어질 블럭 수)를 반환해줍니다.
    2. swap 함수
      맨 마지막 줄부터 순회하면서 값이 0인 좌표에 대해서 해당 열의 값이 0이 아닌 좌표와 값을 스왑합니다.
    3. remove의 갯수가 0이 될때까지 remove 함수와 swap 함수를 반복하며 없어질 블록 수를 카운트합니다.
'''

def solution(m, n, board):
    answer = 0
    brd = [list(line) for line in board]
    sib = [(0, 1), (1, 0), (1, 1)]

    def remove():
        same = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if brd[i][j] == 0:
                    continue
                for x, y in sib:
                    if brd[i][j] != brd[i + x][j + y]:
                        break
                else:
                    same |= {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)}

        for x, y in same:
            brd[x][y] = 0
            
        return len(same)
        
    def swap():
        for i in range(m - 1, 1, -1):
            for j in range(n):
                if brd[i][j] == 0:
                    for k in range(i - 1, -1, -1):
                        if brd[k][j] != 0:
                            brd[i][j], brd[k][j] = brd[k][j], brd[i][j]
                            break

    while True:
        cnt = remove()
        if not cnt:
            return answer
        answer += cnt
        swap()