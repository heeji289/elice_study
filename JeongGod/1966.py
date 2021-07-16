'''
1. 각 들어오는 문서들의 우선순위와 index번호를 튜플형태로 묶어서 deque으로 저장.
2. 따로 우선순위만 갖고 있는 리스트 생성.

만약 deque에 popleft를 했을 경우, 
    '2'에서 생성한 리스트의 끝 값과 우선순위가 같다면
        index를 확인하여 내가 찾는 index라면 
            끝.
        아니라면 
            그대로 진행.
    아니라면
        다시 deque에 add
'''

import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    doc_cnt, doc_idx = map(int ,sys.stdin.readline().split())

    # 우선순위
    idx_list = [i for i in range(doc_cnt)]
    doc_list = list(map(int, sys.stdin.readline().split()))
    # 우선순위만 담은 것을 sort한 것
    priority = sorted(doc_list)
    # 현재 우선순위 들어온 것을 (index, val) 형태로 deque구성
    dq_doc_list = deque(zip(idx_list, doc_list))
    ans = 0
    while dq_doc_list:
        # 우선순위가 낮다면
        if dq_doc_list[0][1] < priority[-1]:
            dq_doc_list.append(dq_doc_list.popleft())
        # 제일 큰 우선순위를 가진 친구라면
        else :
            ans += 1
            if dq_doc_list[0][0] == doc_idx:
                break
            dq_doc_list.popleft()
            priority.pop()
            
    print(ans)
