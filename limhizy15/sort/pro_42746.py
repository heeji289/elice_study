# 가장 큰 수

from functools import cmp_to_key

def solution(numbers):    
    # 정렬에 쓸 비교함수
    def compare(a, b):
        temp_a = a + b
        temp_b = b + a
        
        if temp_a > temp_b:
            return 0
        else:
            return -1
    
    # 요소들을 문자열로 치환
    arr = list(map(str, numbers))
    arr2 = sorted(arr, key=cmp_to_key(compare), reverse=True)
    
    if arr2[0] == 0:
        return '0'
    else:
        return str(int(''.join(arr2)))