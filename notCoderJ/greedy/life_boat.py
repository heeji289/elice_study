'''
  풀이요약
    보트에는 최대 2명씩만 태울 수 있기 때문에 사람들의 몸무게를 정렬하여
    현재 남은 사람들 중 가장 무거운 사람과 가장 가벼운 사람을 계속 짝지으며 보트에 태우는 방법으로 풀이했습니다.
'''

from collections import deque

def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))
    
    while dq:
        if len(dq) > 1 and dq[0] + dq[-1] <= limit:
            dq.popleft()
            dq.pop()
            answer += 1
        else:
            dq.pop()
            answer +=1
    
    return answer