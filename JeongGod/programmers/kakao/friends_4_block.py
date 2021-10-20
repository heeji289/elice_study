def solution(m, n, board):
    answer = 0
    for idx, val in enumerate(board):
        board[idx] = list(val)

    def check_block():
        target = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != "0" and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    target.append((i, j))
        return target

    def break_block(target):
        result = 0
        for i, j in target:
            for x, y in [[0, 0], [0, 1], [1, 0], [1, 1]]:
                if board[i+x][j+y] != "0":
                    board[i+x][j+y] = "0"
                    result += 1
        return result

    def down_block(target):
        """
        1. 세로줄을 리스트로 만든다.
        2. 리스트에서 0의 개수를 세고, 0을 다 없앤다.
        3. 리스트 앞에 0을 붙인다.
        4. 해당 리스트를 다시 세로줄에 붙인다.
        """
        for j in range(n):
            tmp = ""
            zero_cnt = 0
            for i in range(m):
                if board[i][j] == "0":
                    zero_cnt += 1
                else:
                    tmp += board[i][j]
            result = "0"*zero_cnt + tmp
            for i in range(m):
                board[i][j] = result[i]

    while True:
        # 추후에 내릴 때
        target = sorted(check_block(), key=lambda x: x[1])
        if len(target) == 0:
            break
        answer += break_block(target)
        down_block(target)

    return answer
