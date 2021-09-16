import math
from itertools import permutations


def solution(numbers):
    '''
    제곱근을 이용한 소수 판별
    '''
    # 제곱근 소수
    def prime_check(num):
        # 0과 1의 예외처리
        if num < 2:
            return False
        
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    answer = set()
    for i in range(1, len(numbers)+1):
        for com in permutations(numbers, i):
            num = int(''.join(com))
            # 둘 중 하나 사용하면 됩니다.
            
            # 1. 제곱근을 이용한 소수 판별
            if prime_check(num):
                answer.add(num)
            # 2. 에라토스테네스의 체를 이용한 소수 판별
            # if prime[num]:
            #     answer.add(num)

    return len(answer)

from itertools import permutations


def solution(numbers):
    '''
    에라토스테네스의 체를 이용한 소수 판별
    '''
    max_num = int(''.join(sorted(list(numbers), reverse=True)))
    
    # 에라토스테네스의 체
    prime = [True] * (max_num+1)
    prime[0], prime[1] = False, False
    for i in range(2, max_num+1):
        # 방문한 적이 있다면
        if not prime[i]:
            continue
        # 방문한 적이 없다면
        for j in range(i*2, max_num+1, i):
            prime[j] = False
    
    answer = set()
    for i in range(1, len(numbers)+1):
        for com in permutations(numbers, i):
            num = int(''.join(com))

            if prime[num]:
                answer.add(num)
    return len(answer)
