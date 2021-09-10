# 메뉴 리뉴얼

from itertools import combinations
from collections import defaultdict

# orders: 각 손님들이 주문한 것
# course: 코스요리를 구성하는 단품메뉴들의 갯수
def solution(orders, course):
    answer = []
    
    # 코스요리에 필요한 개수 결정
    for c in course:
        comb = defaultdict(int)
        # 주문 조합
        for order in orders:
            # order에서 필요한 요리 개수만큼 조합 구함
            for item in combinations(order, c):
                # 조합을 문자열로 만들고 개수 증가
                temp = ''.join(sorted(item))
                comb[temp] += 1
    
        # 가장 많은 조합 뽑기
        arr = [k for k, v in comb.items() if max(comb.values()) == v]
        # answer에 넣어줌
        for a in arr:
            if comb[a] > 1:
                answer.append(a)
    
    
    return sorted(answer)