'''
    풀이 요약
        해당 문제는 프린터 큐에 들어있는 원소 중 가중치가 높은 순서대로 출력해야 하므로
        큐를 이용해 해결할 수 있을 것 같다. 실제론 다른 방법으로 구해보려고 시도를 많이 해봤지만 잘 해결되지 않았고
        뭔가 구현한 코드가 마음에 들진 않지만 별다른 방법이 떠오르지 않았다ㅠ

        주어진 자료들을 먼저 큐에 모두 넣고 앞에서 하나씩 꺼내며 꺼낸 데이터와 큐에 들어있는 데이터들을 비교해
        꺼낸 데이터보다 큰 가중치를 가진 데이터가 큐에 있으면 다시 큐에 넣고 꺼내기를 반복하며 카운트하는 방식으로 해결하였다.
'''
from collections import deque


test_cnt = int(input())

for _ in range(test_cnt):
    n, m = map(int, input().split())
    nums = deque([v for v in input().split()])
    priority = 0
    idx = m
    cnt = 0
    while nums:
        v = nums.popleft()
        if nums and v < max(nums):
            nums.append((v))
        else:
            priority += 1
            if cnt == idx:
                break

        if cnt == idx:
            idx = len(nums) - 1
            cnt = 0
        else:
            cnt += 1

    print(priority)
