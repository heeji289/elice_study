'''
풀이
1. lock은 padding을 주어서 판의 크기를 늘립니다.(패딩값은 전방향 2*(열쇠 매트릭스 -1)씩 추가)
2. 열쇠는 0, 90, 180, 270도 회전하여 준비합니다.
3. 4종류의 열쇠를 가지고 padding이 추가된 lock 판에서 처음부터 끝까지 완전탐색합니다.(0이상 N+M-1미만)
4. 탐색 시 padding 부분에서는 비교된 값을 무시하며 기존의 lock부분에서는 비교 연산 값이 유효해야 하므로 XOR 연산을 사용합니다.
'''

def rotate(matrix):
    M = len(matrix[0]) 
    result = [ [0] * M for _ in range(M)]

    for r in range(M):
        for c in range(M):
            result[c][M-1-r] = matrix[r][c]

    return result


def make_padding(N, M, lock):
    padding = [[0] * ((N-1) + 2*(M-1))]
    
    # 상단부 패딩 추가
    for _ in range(M-1):
        lock = padding + lock
    
    # lock이 있는 부분에서 좌우 패딩 추가
    for r in range(M-1, N+M-1):
        lock[r] = [0] * (M-1) + lock[r] + [0] * (M-1)
    
    # 하단부 패딩 추가
    for _ in range(N+M-1):
        lock += padding

    return lock

# 완전탐색
def search(key, lock):
    N = len(lock[0]) 
    M = len(key[0]) 

    lock = make_padding(N, M, lock)

    for r in range(N+M-1):
        for c in range(N+M-1):
            for i in range(M):
                for j in range(M):
                    # padding 이전의 lock 범위 안에서 자물쇠와 열쇠가 서로 맞는지 XOR 연산 수행
                    if M-1 <= r+i <= N+M-2 and M-1 <= c+j <= N+M-2 and key[i][j] ^ lock[r+i][c+j] == 0:
                        return False

        return True

def solution(key, lock):

    rotate_90 = rotate(key)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    answer = False
    keys = [key, rotate_90, rotate_180, rotate_270]

    for k in keys:
        if search(k, lock) == True:
            answer = True
    # answer = search(key, lock) | search(rotate_90, lock) | search(rotate_180, lock) | search(rotate_270, lock)

    return answer
