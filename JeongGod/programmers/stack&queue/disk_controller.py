import heapq
from collections import deque
def solution(jobs):
    answer = 0
    # 요청이 들어온 순서대로 정렬
    dq = deque(sorted(jobs))
    hq = []
    cur_time = dq[0][0]

    while dq:
        # 현재 시간중에 요청이 들어온 것을 heapq에 넣는다.
        while dq:
            req, execute = dq[0]
            if req <= cur_time:
                heapq.heappush(hq, (execute, req))
                dq.popleft()
                continue
            break

        # 진행중인 일이 없으면 다음 요청시간까지 점프한다.
        if not hq:
            cur_time = dq[0][0]
            continue
        
        # 일 하나를 처리한다.
        execute, req = heapq.heappop(hq)
        answer += (cur_time - req + execute)
        cur_time += execute

    # 남아있는 일을 처리한다.
    while hq:
        execute, req = heapq.heappop(hq)
        answer += (cur_time - req + execute)
        cur_time += execute

    return answer // len(jobs)
