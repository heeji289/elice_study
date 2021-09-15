from bisect import bisect_left


def solution(citations):
    '''
    h번 이상 인용된 논문이 h편 이상,
    나머지 논문이 h번 이하 인용
    '''
    def poss_check(h):
        result = bisect_left(citations, h)
        return (len(citations) - result) >= h
    answer = 0
    for i in range(10000):
        if poss_check(i):
            answer = i
            continue
        break
    
    return answer

## 미친 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
