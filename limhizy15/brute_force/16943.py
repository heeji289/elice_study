# 숫자 재배치

"""
a, b가 있을 때 a의 순열인 c를 만들것임
가능한 c중에서 b보다 작으면서 가장 큰 값은? c는 0으로 시작할 수 없음

a로 가능한 순열 c를 만들고 이 중 최댓값을 구한다 (b보다 작은)
"""

import sys
from itertools import permutations

input = sys.stdin.readline

a, b = map(int, input().split())
numbers = set()
answer = -1

str_a = str(a)
for comb in permutations(str_a, len(str_a)):
    # print(comb)
    number = ''.join(comb)
    numbers.add(number)

for num in numbers:
    if int(num) <= b and num[0] != '0':
        answer = max(answer, int(num))
# print(a, b)

print(answer)