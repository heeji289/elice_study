## 조합 사용
from itertools import combinations

answer = 0
def solution(relation):
    # 유일성 체크
    def uni_check(idxs):
        tmp = set()
        for row in relation:
            tmp.add(tuple(row[int(idx)] for idx in idxs))
            # 길이가 같다면 유일성 만족
        return len(tmp) == len(relation)
    
    # 최소성 체크
    visited = []
    def mini_check(idxs):
        for v in visited:
            # 만약 합집합을 했는데 길이가 같다면 최소성을 만족못한다.
            # ex) v = (2,4) idxs = (2,3,4)
            if len(idxs) == len(v | set(idxs)):
                return False
        visited.append(set(idxs))
        return True
    
    # 전체 체크
    def dfs(rel_idx, cnt):
        global answer
        # 다 둘러봤다면
        if cnt > len(relation[0]):
            return
        for com in combinations(rel_idx, cnt):
            # 해당 조합이 유일성을 만족한다면
            # (0), (2,3), (1,3,4)
            if uni_check(com) and mini_check(com):
                print(com)
                answer += 1
        dfs(rel_idx, cnt+1)
    
    
    dfs(set(range(len(relation[0]))), 1)
    
    return answer

## Bitmask
def solution(relation):
    '''
    비트마스크 => 00000000(컬럼의 개수)
    '''
    answer = 0
    # bit => col의 번호로 변경
    def bit_to_col(bit):
        result = []
        col = 0
        while bit:
            if bit%2 != 0:
                result.append(col)
            bit >>= 1
            col += 1
        return result
    # 유일성 체크
    def uni_check(idxs):
        tmp = set()
        for row in relation:
            tmp.add(tuple(row[int(idx)] for idx in bit_to_col(idxs)))
            # 길이가 같다면 유일성 만족
        return len(tmp) == len(relation)
    
    # 최소성 체크
    def mini_check(idxs):
        for v in visited:
            if v & idxs == v :
                return False
        return True
    
    visited = []
    for i in range(1<<len(relation[0])):
        if uni_check(i) and mini_check(i):
            visited.append(i)
            answer += 1
    
    return answer
