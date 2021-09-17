'''
  풀이 요약
    현재 괄호가 올바른 괄호인지 판단하는 함수와 u, v로 나누는 함수, 괄호를 뒤집는 함수 3개의 함수를 만든 후
    초기 괄호가 올바른 괄호면 바로 반환을 하고
    아닌 경우 주어진 절차를 계속 반복하면서
    u가 올바른 괄호면 front에 추가해주고
    아닌 경우 front에는 '('를 back에는 ')' + 뒤집은 괄호를 추가해줍니다.
    v가 빈문자열이 되었을 때 front와 back을 합하여 반환합니다.
'''

def solution(p):
    # 올바른 괄호 판별
    def normal(paren):
        if not paren:
            return True
        
        st = 0
        for p in paren:
            if p == '(':
                st += 1
            elif st == 0:
                return False
            else:
                st -= 1
        return False if st else True
    
    # u, v 분리
    def split_paren(paren):
        st = 0
        for i, p in enumerate(paren):
            st += 1 if p == '(' else -1
            if not st:
                return (paren[:i + 1], paren[i + 1:])
        return (paren, '')
    
    if normal(p):
        return p
    
    # 뒤집기
    rev = lambda x: ''.join([('(', ')')[n == '('] for n in x[1:-1]])
    
    paren = p
    front, back = '', ''
    while True:
        u, v = split_paren(paren)
        if normal(u):
            front += u
            paren = v
        else:
            front += '('
            back = ')' + rev(u) + back
            paren = v
        if not v:
            return front + back