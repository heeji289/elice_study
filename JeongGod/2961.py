# 10개밖에 안주어진다. Brute Force도 생각.
import sys, math
from itertools import combinations
input = sys.stdin.readline

n = int(input())

gred = []
for _ in range(n):
    gred.append(tuple(map(int, input().split())))

ans = math.inf
for i in range(1,n+1):
    tmp = list(combinations(gred, i))
    for total in tmp: # 조합중 1개 선택
        a,b = 1,0
        for elem in total: # 선택된 친구들을 계산
            a *= elem[0]
            b += elem[1]
        ans = min(ans, abs(a-b))
print(ans)

