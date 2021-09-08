'''
  풀이요약
    1. 주어진 작업들을 요청된 순서에 맞게 정렬해줍니다.
    2. 해당 작업들을 작업 queue에 모두 넣어주고 작업 대기 큐를 생성해줍니다.
    3. 전체 작업이 끝나는 시간 동안 반복하면서
      현재 시간과 작업 요청시간이 동일한 작업들을 작업 큐에서 꺼내 작업 대기 큐에 넣어주고
      현재 시간이 현재 진행 중인 작업이 끝나는 시간과 같거나 큰 경우 작업 대기 큐에서 소요시간이 가장 적은 작업을 하나 꺼내 처리 시간을 누적해줍니다.
    4. 모든 작업들의 누적된 처리 시간을 작업 수로 나눈 값을 반환합니다.
'''
import heapq
from collections import deque


def solution(jobs):
    answer = 0
    schedule = []
    total = sum([job[1] for job in jobs])
    tasks = deque(sorted(jobs, key=lambda x: x[0]))
    
    end = 0
    for current in range(total):
        while tasks and tasks[0][0] == current:
            req, need = tasks.popleft()
            heapq.heappush(schedule, (need, req))
        if current >= end and schedule:
            take, request = heapq.heappop(schedule)
            end = current + take
            answer += end - request

    return answer // len(jobs)