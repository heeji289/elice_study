'''
  풀이요약
    모든 주문에 대해서 주어진 코스의 조합 갯수별로 요리 조합을 모두 구하여 각 요리 조합을 선택한 사람 수를 구합니다.
    선택한 사람의 수가 2이상인 요리 조합들 중 각 코스 갯수별 최대 선택 요리 조합들만 추출하여 반환해줍니다.
'''
from itertools import combinations
from functools import reduce
from collections import defaultdict


def solution(orders, course):
    menus = defaultdict(int)
    best_cnt = {cnt: 0 for cnt in course}
    best_menu = {cnt: [] for cnt in course}
    for order in orders:
        for cnt in course:
            for cuisine in combinations(order, cnt):
                menus[''.join(sorted(cuisine))] += 1
    for menu, people in filter(lambda x: x[1] >= 2, menus.items()):
        if people > best_cnt[len(menu)]:
            best_cnt[len(menu)] = people
            best_menu[len(menu)] = [menu]
        elif people == best_cnt[len(menu)]:
            best_menu[len(menu)].append(menu)
            
    return sorted(reduce(lambda x, y: x + y, best_menu.values()))