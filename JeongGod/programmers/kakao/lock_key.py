def solution(key, lock):
    """
    열쇠의 홈과 돌기는 자물쇠에 영향을 주지 않는다.
    자물쇠의 홈 == 열쇠의 돌기 부분 일치
    자물쇠의 돌기와 열쇠의 돌기가 만나서는 안된다.
    자물쇠의 홈을 다 채워야 열 수 있다.

    열쇠는 회전과 이동이 가능하다.
    0 : 홈 부분, 1은 돌기 부분

    1. M + N + M크기의 보드를 만든다.
    2. 자물쇠를 한 가운데에다가 놓는다.
    3. 열쇠를 해당 보드에 넣어서 가능한지 판단한다.
    4. 회전을 시킨다.
    5. 가능한지 판단한다.
    40*40*20*20 64만의 시간복잡도
    """
    N, M = len(lock), len(key)
    # 2*M + N사이즈의 보드를 만듦
    board = [[-1] * (N + 2*M) for _ in range(N + 2*M)]
    T = len(board)
    # lock을 보드 가운데에다가 놓음
    for x in range(M, M+N):
        for y in range(M, M+N):
            board[x][y] = lock[x-M][y-M]

    # 자물쇠가 모두 1이 되었다면 열림.
    def key_check():
        for lx in range(M, M+N):
            for ly in range(M, M+N):
                if board[lx][ly] != 1:
                    return False
        return True

    # 자물쇠에 키를 넣어본다.
    def key_insert(bx, by):
        # key 순회
        for kx in range(M):
            for ky in range(M):
                board[bx+kx][by+ky] += key[kx][ky]

    # 자물쇠에서 키를 뺀다.
    def key_pop(bx, by):
        for kx in range(M):
            for ky in range(M):
                board[bx+kx][by+ky] -= key[kx][ky]

    # 키를 회전시킨다.
    def key_rotate():
        tmp = [[0] * M for _ in range(M)]
        for kx in range(M):
            for ky in range(M):
                tmp[kx][ky] = key[ky][M-kx-1]
        return tmp

    for i in range(4):
        # 보드 순회
        for bx in range(1, T-M):
            for by in range(1, T-M):
                key_insert(bx, by)
                if key_check():
                    return True
                key_pop(bx, by)

        key = key_rotate()

    return False
