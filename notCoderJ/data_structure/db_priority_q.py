'''
  풀이요약
    최대 힙과 최소 힙 2개의 힙을 생성하고 현재 데이터의 갯수를 카운팅할 딕셔너리를 생성해서 연산을 수행했습니다.
    자료의 삽입 명령인 경우 최대 힙과 최소 힙에 모두 넣어주고 카운트 딕셔너리의 해당 값을 key로 하는 값으 1 증가시켜 줍니다.
    삭제 연산인 경우 각 경우에 대해 최대 힙이나 최소 힙 둘 중 하나의 힙에서 자료를 삭제하고 카운트 딕셔너리를 갱신해줍니다.
    모든 연산을 수행 후 카운트가 0이 아닌 값들(key)만 필터링한 후 값이 있으면 [최댓값, 최솟값]을 출력하고 없으면 [0, 0]을 출력했습니다.
    
    다른 분들의 풀이를 보다가 좋은 풀이가 있어서 2개정도 가져와봤습니다.
    - 풀이 2
      heapq의 성질을 잘이용한 풀이네요.
      최소힙을 하나 구현하여 해당 힙에 주어지는 자료들을 모두 넣어줍니다.
      삭제 연산의 경우 최솟값을 빼줄 때에는 heapq의 heappop 연산을 수행하고
      최댓값을 빼줄 때에는 list의 remove 연산을 통해 힙의 최대값을 지정하여 삭제해줍니다.
      이렇게 해도 가능한 이유는 힙에서 remove연산을 수행해도 결국 리스트이기 때문에 현재 최솟값의 위치는 변하지 않고, heappush가 수행되면 heap을 다시 유지시켜주기 때문에 가능한 풀이같습니다.
    
    - 풀이 3
      이 풀이는 제가 풀었던 것과 같이 최소 힙과 최대 힙 2개의 힙을 사용한 방법인데요.
      제가 딕셔너리를 만들어서 두 힙의 데이터를 동기화했던 방법과 달리 각 힙의 첫번째 요소를 비교해서 동기화해준 방법입니다.
      이 방법이 제 방법보다 좀 더 코드가 간결하고 좋은 것 같아서 가져와봤습니다.
'''

import heapq
from collections import defaultdict


# 제 풀이입니다.
def solution(operations):
    max_hq, min_hq = [], []
    count = defaultdict(int)
    size = 0

    def delete(cmd):
        nonlocal size
        while size:
            d = heapq.heappop([max_hq, min_hq][cmd < 0])
            d = d if cmd < 0 else -d
            if count[d]:
                count[d] -= 1
                size -= 1
                break

    for op in operations:
        cmd, val = op.split()
        val = int(val)
        if cmd == 'I':
            heapq.heappush(max_hq, -val)
            heapq.heappush(min_hq, val)
            count[val] += 1
            size += 1
        else:
            delete(val)

    remain = list(filter(lambda x: x[1] != 0, count.items()))
    return [0, 0] if not remain else [max(remain)[0], min(remain)[0]]


def solution(operations):  # 풀이 2
    hq = []

    for op in operations:
        cmd, val = op.split()
        val = int(val)
        if cmd == 'I':
            heapq.heappush(hq, val)
        elif hq:
            heapq.heappop(hq) if val < 0 else hq.remove(max(hq))

    return [0, 0] if not hq else [max(hq), heapq.heappop(hq)]


def solution(operations):  # 풀이 3
    max_hq, min_hq = [], []

    def delete(val):
        nonlocal max_hq, min_hq
        hq = [min_hq, max_hq][val > 0]
        if not hq:
            return
        heapq.heappop(hq)
        if not hq or -max_hq[0] < min_hq[0]:
            min_hq, max_hq = [], []

    for op in operations:
        cmd, val = op.split()
        val = int(val)
        if cmd == 'I':
            heapq.heappush(max_hq, -val)
            heapq.heappush(min_hq, val)
        else:
            delete(val)

    return [0, 0] if not min_hq else [-heapq.heappop(max_hq), heapq.heappop(min_hq)]
