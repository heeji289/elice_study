# [kakao blind 2018 3차] 압축

"""
1. 탐색 중인 위치를 pos로 둔다.
2. pos를 시작으로 다음 문자들을 더해보면서 사전에 있는지 체크한다.
 - 사전에 없으면 그 위치 이전것까지가 w가 되고 그 다음이 c가 된다 (pos를 c위치로 갱신)
3. w + c로 새롭게 사전에 등록하고 반복 (인덱스를 저장할 변수도 필요)
"""
from collections import defaultdict

def solution(msg):
    answer = []
    
    # A to Z 사전 초기화
    dictionary = defaultdict(int)
    
    start = 65
    for i in range(26):
        temp = start + i # ASCII 
        dictionary[chr(temp)] = i + 1
    
    max_index = 26 # 지금까지 사전의 마지막 색인 번호 

    pos = 0
    target = ''
    while pos < len(msg):
        target += msg[pos]

        if target in dictionary:
            pos += 1
            continue

        # 사전에 없는 경우
        w = target[:-1]
        answer.append(dictionary[w])

        max_index += 1
        dictionary[target] = max_index

        target = ''

    # 마지막 문자 예외처리 😤
    answer.append(dictionary[target])
    
    return answer

print(solution('KAKAO'))