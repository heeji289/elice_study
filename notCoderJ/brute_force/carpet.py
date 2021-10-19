'''
  풀이요약
    1. 카펫의 전체 격자 갯수를 구한 후 해당 수의 약수를 탐색합니다.
    2. 약수가 a, b라 할 때 노란 격자의 수 == (a-2)(b-2)를 만족하는 약수를 출력합니다.
'''

import math

def solution(brown, yellow):
    total = brown + yellow
    for w in range(3, int(math.sqrt(total)) + 1):
        q, r = divmod(total, w)
        if r == 0 and (w - 2) * (q - 2) == yellow:
            return sorted([w, q], reverse=True)