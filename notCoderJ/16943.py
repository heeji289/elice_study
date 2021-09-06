'''
    풀이 과정:
        주어진 A값의 범위는 크지만 자릿수는 최대 10자리이므로 A에 대한 순열을 구해서
        B값과 하나씩 비교하며 B보다 작은 값 중 큰 값을 출력하면 되겠다고 생각했습니다.
        
        1. A값에 중복 값이 있는 경우 순열을 구하면 중복된 값이 나오기 때문에 A의 순열을 구해서 집합으로 만들었습니다.
        2. 1번에서 구한 순열을 순회하며 첫 자리가 0으로 시작하지 않고 B값보다 작은 값 중 최댓값을 구했습니다.
'''

from itertools import permutations
import sys

input = lambda: sys.stdin.readline().rstrip()


answer = -1
a, b = input().split()

for v in set(permutations(a)):
    c = ''.join(v)
    if c[0] != '0' and int(c) <= int(b):
        answer = max(answer, int(c))
        
print(answer)