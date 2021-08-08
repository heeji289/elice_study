# N과 M (1)

"""
1부터 n까지 자연수 중 중복 없이 m개를 고른 수열
"""
import sys
from itertools import permutations

input = sys.stdin.readline

# n, m 입력
n, m = map(int, input().split())

_set = [i+1 for i in range(n)]
# n개의 집합에서 m개를 고르는 순열을 구한다
comb = permutations(_set, m)

# answer = []
# for item in comb:
#     temp = []
#     for i in item:
#         temp.append(i)
#     answer.append(temp)

# # 정렬한다
# answer.sort()
# for item in answer:
#     for i in item:
#         print(i, end=' ')
#     print()

# 출력이 영..
for item in comb:
    print(' '.join(map(str, item))) # tuple -> str