'''
1,000,000,000이여도 숫자를 조합하기 때문에 자릿수가 중요하다. 따라서, 최대 10개를 가지고 구한다.
순열은 O(n!)이기 때문에  10! = 3,628,800이다.
전체 시간복잡도는 O(n*n!)으로 36,288,000으로 충분하다.

1. 순열을 이용하여 모든 경우의 수를 구한다.
2. 해당 경우의 수를 숫자로 바꾼다.
    2-1 만약 처음시작이 0으로 시작한다면, 버린다.
3. 숫자를 비교하여 큰 값을 넣는다.

'''
import sys
from itertools import combinations,permutations
input = sys.stdin.readline

a, b = map(int, input().split())
a = str(a)

ans = -1
for i in permutations(a, len(a)):
    tmp = ""
    if i[0] == '0':
        continue
    for j in i:
        tmp += j
    com = int(tmp) if len(tmp) > 0 else -1
    if b >= com:
        ans = max(ans, com)
print(ans)