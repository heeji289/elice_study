# 소-난다!

"""
[문제]
꿀벌에 쏘이면 소가 잠깐 날 수 있다..
농장에 N마리 중 M마리를 선별해 몸무게 합이 소수가 되도록 하고싶다.
나올 수 있는 몸무게 합은?

[풀이]
1. N개 중 M개 선택하는 순열을 구하고
2. 이들의 합이 소수인지 판별하고 => 에라로 합의 최소부터 최대까지 소수 판별해놓고 나중에 확인
3. 저장..
"""
import sys
from itertools import permutations

input = sys.stdin.readline

# n, m 입력
n, m  = map(int, input().split())

# n개의 소 몸무게 배열에 저장
cows = list(map(int, input().split()))

# n개 중 m개 순열 찾아서
# 몸무게 합을 배열에 저장
allSum = []
for comb in permutations(cows, m):
    _sum = sum(comb)
    allSum.append(_sum)

# 중복제거
allSum = set(allSum)

allSum_max = max(allSum)
# 몸무게 합 최소부터 최대까지 소수판별
primes = [True, True] + [False] * (allSum_max+1)

for i in range(2, allSum_max+1):
    if not primes[i]:
        j = i + i
        while j <= allSum_max:
            primes[j] = True
            j += i

# 몸무게 합 중 최소인 것만 선택해서 정답 배열에 저장
allSum = list(allSum)
answer = []
for i in range(len(allSum)):
    if not primes[allSum[i]]:
        answer.append(allSum[i])

answer.sort()
# 정답 배열 출력
if len(answer) != 0:
    for item in answer:
        print(item, end=" ")
# 비었으면 -1 출력
else:
    print(-1)