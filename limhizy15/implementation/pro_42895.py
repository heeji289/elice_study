# 5와 사칙연산을 사용해서 number를 만들 때 N의 최솟값은?

def solution(N, number):
    answer = 0 
    
    # 자기자신
    if N == number:
        return 1
    
    # [{5}, {55}, {555}, ...] 이런 식으로 집합의 배열 생성
    s = [set() for i in range(8)]
    for i, x in enumerate(s, start = 1):
        x.add(int(str(N) * i))
    
    # 할 수 있는 연산을 모두해서 집합에 넣는다
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        # 만들 수 있으면 최소값을 저장
        if number in s[i]:
            answer = i + 1
            break
                        
    else:
        answer = -1
    
    return answer