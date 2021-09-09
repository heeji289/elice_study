from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    '''
    가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구 성
    2가지 이상, 2명 이상의 주문의 단품메뉴 후보
    '''
    _dict = defaultdict(int)
    # 손님이 시킨 메뉴에서 모든 조합을 알아본다.
    for order in orders:
        for n in course:
            for i in combinations(sorted(list(order)), n):
                _dict[i] += 1

    results = sorted(_dict.items(), key=lambda x: x[1], reverse=True)
    # "오름차순"으로 주어진다고 했으므로 course[-1]이 최댓값
    course_dict = defaultdict(int)
    for num in course:
        # 최소 2명 이상의 손님에게 주문받은것만 가능
        course_dict[num] = 2

    answer = []
    for menu, cnt in results:

        # 먼저 course에 해당하는 개수인지 확인 => 현재 course에서 요구하는 최대메뉴가 맞는지 확인
        if len(menu) in course_dict and cnt >= course_dict[len(menu)]:
            course_dict[len(menu)] = cnt
            answer.append(''.join(menu))

    return sorted(answer)

## Counter 사용
import collections
import itertools


def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
