'''
  풀이요약
    프로그래머스에서는 풀지 않았는데, 저번 스터디 때 백준에서 풀었던 기억이 어렴풋이 나네요.
    풀이를 생각해보다가 아마 정규님 풀이였나요? 매번 가장 높은 우선 순위의 작업을 계산하지 않고
    처음에 정렬해놓고 비교하는 방식이 생각나서 그 방식으로 풀어봤습니다.
  
    1. 작업 순서를 내림차 정렬하여 deque에 저장합니다.
    2. 알기 원하는 작업을 표시하여 주어진 작업을 순서대로 deque에 저장합니다.
    3. 2번의 deque에서 하나씩 꺼내 1번 deque의 0번째 원소, 즉 가장 우선순위가 높은 작업과 일치하는지 확인합니다.
      3-1. 일치한다면 answer값을 1 증가시키고 현재 작업이 marking된 작업인지 확인하여 맞다면 answer값을 반환합니다.
      3-2. 일치하지 않는다면 다시 2번 deque의 맨 뒤에 넣고 3번 과정을 반복합니다.
'''
from collections import deque


def solution(priorities, location):
    answer = 0
    order = deque(sorted(priorities, reverse=True))
    dq = deque([(v, [False, True][i == location]) for i, v in enumerate(priorities)])
    
    while dq:
        priority, job = dq.popleft()
        if priority != order[0]:
            dq.append((priority, job))
            continue
            
        answer += 1
        if job:
            return answer
        order.popleft()