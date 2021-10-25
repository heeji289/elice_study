# 비밀지도를 해독해서 #과 공백으로 만들어라
"""
1. 숫자를 1, 0으로 추출하고 => 이진법
2. or 하면 될 듯

9  = 01001
30 = 11110

30 / 2 = 15 ..0 / 2 = 7 ..1 / 2 = 3 ..1 / 2 = 1 .. 1 / 2 = 0 ..1
"""

def convert2binary(n, number):
    converted = ''
    while number != 0:
        converted = str(number % 2) + converted
        number = number // 2
    
    if len(converted) != n:
        converted = '0' * (n - len(converted)) + converted
    return converted

def solution(n, arr1, arr2):
    answer = []
    
    a1 = [[0] * n for _ in range(n)]
    a2 = [[0] * n for _ in range(n)]
    
    for i in range(n):
        binary = convert2binary(n, arr1[i])
        for j in range(n):
            a1[i][j] = int(binary[j])
    
    for i in range(n):
        binary = convert2binary(n, arr2[i])
        for j in range(n):
            a2[i][j] = int(binary[j])
    
    for i in range(n):
        temp = ''
        for j in range(n):
            _or = a1[i][j] | a2[i][j]
            if _or == 0:
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
            
    return answer