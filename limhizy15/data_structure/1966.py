# 프린터 큐 asdf

'''
[문제]
우선순위를 가진 문서가 순서대로 주어진다. 
대기열에 있는 가장 높은 우선순위의 문서가 항상 먼저 출력된다.
문서 번호가 주어질 때 해당 문서가 몇 번째에 출력되는지 찾아라.

[풀이]
1. 큐 front의 중요도를 확인한다.
-> 가장 높은 중요도를 가지면 그대로 출력
-> 아니면 큐의 맨 뒤로 옮긴다.
2. 찾고자 하는 문서가 출력될 차례가 되면 반복문을 종료하고 출력
'''

from collections import deque

tc = int(input())
for _ in range(tc):
    # 문서의 수, 궁금한 문서의 위치
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dq = deque() # 우선순위
    idx = [] # 원래 인덱스
    # dq에 [5] idx에 [0] => 얘네 같이 움직여야함
    for i in range(n):
        dq.append(arr[i])
        idx.append(i)

    cnt = 0
    # dq가 빌 때까지 반복
    while dq:
        # dq의 맨 앞 요소의 우선순위가 최댓값이라면
        if dq[0] == max(dq):
            # 맨 앞 거 프린트해줌
            pop_idx = idx[0]
            dq.popleft()
            del idx[0]
            cnt += 1
            # 이 인덱스가 찾고자하는 문서라면 print하고 break
            # 아니면 계속..
            if pop_idx == m:
                print(cnt)
                break
        else:
            # dq의 맨 앞 요소의 우선순위가 최댓값이 아니라면
            # popleft하고 append
            cur_priority = dq[0]
            cur_idx = idx[0]
            dq.popleft()
            del idx[0]

            dq.append(cur_priority)
            idx.append(cur_idx)