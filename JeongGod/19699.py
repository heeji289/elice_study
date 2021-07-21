'''
m개를 뽑았을때의 합이 소수가 되도록 하여라
해당 소수들을 리스트에 담는다.
소수는 오름차순으로 출력한다.
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

cow = list(map(int, input().split()))

# 아리토스테네스의 채 이용
prime = [True for i in range(9001)]
for i in range(2,9001):
    for j in range(2*i, 9001, i):
        if prime[j]:
            prime[j] = False

_set = set()
for elems in combinations(cow, m):
    result = 0
    for elem in elems:
        result += elem
    if prime[result]:
        _set.add(result)


print(" ".join(map(str, sorted(_set))) if len(_set) > 0 else -1)
