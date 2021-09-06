'''
  풀이요약
    1. 주어진 옷을 종류에 따라 갯수를 카운팅합니다.
    2. 각 갯수에 1을 더한 후(선택하지 않는 조건) 모든 종류의 갯수를 곱해주고 모두 선택하지 않는 경우인 1을 빼줍니다.
'''
from functools import reduce
from collections import Counter


def solution(clothes):
    types = Counter([type for _, type in clothes])
    return reduce(lambda x, y: x * y, map(lambda x: x + 1, types.values())) - 1
