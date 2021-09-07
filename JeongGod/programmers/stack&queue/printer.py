from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque(zip(range(len(priorities)), priorities))
    prior_list = sorted(priorities)

    while dq:
        loc, prior = dq.popleft()

        if prior_list[-1] > prior:
            dq.append((loc, prior))
            continue        
        # 인쇄가능하다면
        prior_list.pop()
        answer += 1
        if loc == location:
            return answer
        
    return answer
