from collections import defaultdict
from functools import reduce
from itertools import combinations


def solution(clothes):
    _dict = defaultdict(int)
    
    for _, kind in clothes:
        _dict[kind] += 1
    
    num = _dict.values()
    
    ans = 0
    # 조합의 개수 세기 (시간 초과)
    # for i in range(1, len(num)+1):
    #     for com in combinations(num, i):
    #         ans += reduce(lambda x, y: x*y, com)
            
    ans += reduce(lambda x, y: x*y, [i+1 for i in num])
    
    return ans-1
