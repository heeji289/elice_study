# 2020 KAKAO 괄호변환

def is_correct(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(': cnt += 1
        else: cnt -= 1
        # cnt가 음수가 되면 짝이 안맞으므로 False
        if cnt < 0: return False
    
    # 마지막에 한 번 더 체크
    if cnt == 0: return True

def solution(p):
    answer = ''
    
    # 1. 빈 문자열이면 그대로 반환
    if len(p) == 0: return p
    
    cnt = 0
    u, v = '', ''
    
    # 2. 균형잡힌 u, 나머지 v로 분리
    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        else: cnt -= 1
        
        if cnt == 0:
            u = p[0:i+1]
            v = p[i+1:]
            # print('what', u, v)
            break
    
    # 3. u가 올바른이면
    if is_correct(u):
        # 3-1. v에 대해 1부터 수행하고 u에 더한 뒤 반환
        return u + solution(v)
    
    # 4. u가 올바른이 아니면
    # 4-1 ~ 4-3
    empty = '' # error 
    empty += '(' + solution(v) + ')'
    # 4-4. u의 처음과 끝 제거 후 뒤집기
    for i in range(1, len(u) - 1):
        empty += '(' if u[i] == ')' else ')'
    return empty