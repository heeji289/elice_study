# [완전탐색] 소수 찾기

'''
종이의 숫자들로 만들 수 있는 소수의 개수는 
1. 숫자 배열의 순열을 구한다. 
2. 소수인지 판별한다.
'''
from itertools import permutations
import math

def is_prime(x):
    if x < 2: return False
    
    for i in range(2, x):
        if x % i == 0: return False
    return True

def solution(numbers):
    answer = 0
    
    arr = [i for i in numbers]
    arr.sort(reverse=True) # 혹시모르니까 역순정렬
    
    s = set()
    
    for size in range(1, len(arr) + 1):
        for item in permutations(arr, size):
            s.add(int(''.join(item)))
    
    # 소수 판별      
    for item in list(s):
        if is_prime(item): answer += 1
        
    return answer