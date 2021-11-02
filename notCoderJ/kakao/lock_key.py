'''
  풀이요약
    1. 열쇠의 1의 좌표 값들과 자물쇠의 0의 좌표 값들을 저장합니다.
    2. 90도씩 총 4번(원점 포함) 회전하며 다음 연산을 수행합니다.
    3. 상하좌우 최대 n - 1번(n >= m)의 이동이 가능하므로 -(n-1)부터 n-1까지 반복하며
      행과 열 변화량을 열쇠의 좌표에 합해 변화된 좌표 값을 구합니다.
    4. 구한 좌표 값들과 슬롯의 좌표 값들이 모두 일치한다면 True를 반환합니다.
'''
def solution(key, lock):
    answer = False
    m, n = len(key), len(lock)

    def spinNslot(x, target, val):
        result = set()
        for i in range(x):
            for j in range(x):
                if target[i][j] == val:
                    result.add((i, j))
        return result
    
    def rotate(spin):
        result = set()
        for i, j in spin:
            result.add((j, m - i - 1))
        return result
    
    spin, slot = spinNslot(m, key, 1), spinNslot(n, lock, 0)
    for _ in range(4):
        spin = rotate(spin)
        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):
                valid = set()
                for i, j in spin:
                    if 0 <= i + dx < n and 0 <= j + dy < n:
                        valid.add((i + dx, j + dy))
                if valid == slot:
                    return True
    
    return answer