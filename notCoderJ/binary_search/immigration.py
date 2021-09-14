'''
  풀이 요약
    1. 모든 사람이 검사를 마친 최대 시간을 구합니다. == 최대 심사 시간 * (입국자 / 심사자)
    2. 이분 탐색을 수행하며 매번 처리 시간을 반토막내고, 해당 시간에 각 심사원들이 처리한 입국자 수를 구해 합하고
      그 수와 총 입국자의 수를 비교합니다.
      2-1. 만약 같거나 넘는다면 answer값을 현재 중앙값으로 갱신하고 중앙값의 좌측에 대해 2번 과정을 재수행합니다.
      2-2. 만약 작다면 중앙값의 우측에 대해 2번 과정을 재수행합니다.
'''

def solution(n, times):
    answer = 0
    # 1. max time을 구합니다.
    t_max = max(times) * (sum(divmod(n, len(times))))
    
    # 2. 이분탐색을 수행하며, 최종 처리 시간을 구합니다.
    def bi_search(start, end):
        nonlocal answer
        if start > end:
            return
        
        mid = (start + end) // 2
        processed = sum(map(lambda x: mid // x, times))
        if processed >= n:
            answer = mid
            bi_search(start, mid - 1)
        else:
            bi_search(mid + 1, end)
    
    bi_search(0, t_max)
    
    return answer