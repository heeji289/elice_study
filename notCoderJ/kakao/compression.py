'''
  풀이 요약
    문제에서 주어진대로 하나씩 비교해보면서 사전을 만들어 압축하는 방식으로 풀었습니다.
    1. string의 영문 대문자 문자열을 가져와서 초기 길이가 1인 사전을 만들어줍니다.
    2. 주어진 문자열을 하나씩 돌며, 현재 문자를 이어붙이고 사전에 있는지 확인합니다.
    3. 만약 사전에 현재 이어붙인 문자열이 존재하지 않으면
      해당 문자열의 끝문자를 제외한 나머지 문자열을 사전에서 찾아 값으로 추가하고
      해당 문자열을 사전에 등록 후 이어붙인 문자열을 문자열의 끝문자로 초기화합니다.
    4. 변환을 마친 후 남은 문자열이 있으면 사전에서 변환하여 추가해줍니다.
'''

import string

def solution(msg):
    answer = []
    lzw = {w: i + 1 for i, w in enumerate(string.ascii_uppercase)}
    next = 27
    
    comp = ''
    for c in msg:
        comp += c
        if comp not in lzw:
            answer.append(lzw[comp[:-1]])
            lzw[comp] = next
            comp = comp[-1]
            next += 1
    
    return answer if not comp else answer + [lzw[comp]]