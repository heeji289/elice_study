'''
3개를 무조건 선택한다.
100, 100, 100 => 1000000만번
3중 포문 가능.

1. 빈 집합 리스트에 안되는 조합을 추가한다.
2. 첫번째 친구를 선택한 뒤, 두번째 친구는 첫번째 친구와 조합이 되는지 본다.
3. 세번쨰 친구는 첫번째, 두번쨰 친구와 조합이 되는지 본다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

combination = [set() for _ in range(n+1)]

for _ in range(m):
    tmp = list(map(int, input().split()))
    combination[tmp[0]].add(tmp[1])
    combination[tmp[1]].add(tmp[0])

ans = 0
for i in range(1,n+1): # 첫번째 선택
    for j in range(i+1,n+1): # 두번쨰 선택
        if j in combination[i]:
            continue
        for k in range(j+1,n+1): # 세번째 선택
            if k in combination[j] or k in combination[i]:
                continue
            ans += 1
print(ans)