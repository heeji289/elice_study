def solution(p):
    '''
    항상 ( )의 개수는 같다.
    '''
    # 균형 체크
    def bal_check(p):
        cnt, other_cnt = 0, 0
        idx = 0
        # 균형잡힌 문자열 구하기
        for idx in range(len(p)):
            # 괄호의 개수를 센다
            if p[0] == p[idx]:
                cnt += 1
            else:
                other_cnt += 1
            # 더 이상 분리할 수 없어야 한다.
            if cnt == other_cnt:
                break
        return (p[:idx+1], p[idx+1:])
    
    # 올바른지 체크
    def yes_check(p):
        stack = []
        for i in range(len(p)):
            if p[i] == "(":
                stack.append(p[i])
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
    
    # 뒤집기
    def reverse_shape(u):
        tmp = ""
        for i in u[1:-1]:
            if i == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp
    
    def dfs(p):
        # 균형 체크
        u, v = bal_check(p)
        
        print(f"u = {u}, v = {v}")
        # u 올바른지 체크
        if yes_check(u):
            # u가 올바르고 v가 빈 문자열이라면 끝
            if v == "":
                return u
            # u가 올바르고 v가 비어있지 않다면 v 반복
            return u + dfs(v)
        # 괄호 모양을 뒤집는거였따..
        tmp = ""
        tmp += "(" + dfs(v) + ")" + reverse_shape(u)
        return tmp
    
    return p if yes_check(p) else dfs(p)
