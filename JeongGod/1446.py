'''
전에 풀었던 회의? 최대 많은 회의를 할 수 있는 걸 고르는 문제가 생각났습니다.
그래서 풀었던 방법을 떠올려 비슷하게 풀어봤습니다.
'''

# import sys
# input = sys.stdin.readline

# n, d = map(int, input().split())
# short = sorted([list(map(int, input().split())) for i in range(n)])
# ans = d
# def dfs(start, cur, cost):
#     global ans
#     # 도착했다면.
#     if cur == d:
#         ans = min(ans, cost)
#     # 지름길을 다 탐색했지만 도착하지 못했다면
#     if start == len(short):
#         # 현재 거리는 도착 거리보다 작아야 한다. 답은 지금까지 (비용 + 남은 거리 비용)
#         if cur < d:
#             ans = min(ans, cost+(d-cur))
#         return    

#     for i in range(start, len(short)):
#         # 지름길의 시작점이 현재보다 작거나, 목적지를 넘어서는 지름길이라면
#         if short[i][0] < cur or short[i][1] > d:
#             continue
#         # 지름길의 시작점까지 이동한 비용
#         tmp = short[i][0] - cur
#         # 지름길로 가는 것보다 그냥 가는것이 낫다면
#         if short[i][2] > short[i][1] - short[i][0]:
#             tmp += short[i][1] - short[i][0]
#         else:
#             tmp += short[i][2]
#         print(f"i: {i}, cur: {short[i][1]}, short_cost: {short[i][2]} cost: {cost+tmp}")
#         dfs(i+1, short[i][1], cost+tmp)
# dfs(0, 0, 0)
# print(ans)

'''
DP 
dp[i] = min(dp[i-1] + 1 , dp[지름길 start index] + 지름길 cost)
'''

import sys
from collections import defaultdict
input = sys.stdin.readline

n, dest = map(int, input().split())
short = defaultdict(list)
for i in range(n):
    s_start, s_dest, s_cost = map(int, input().split())
    short[s_dest].append((s_start, s_cost))

dp = [0]
for idx in range(1,dest+1):
    if idx in short:
        tmp = 1e9
        for elem in short[idx]:
            tmp = min(tmp, dp[elem[0]] + elem[1])
        dp.append(min(dp[idx-1]+1, tmp))
    else :
        dp.append(dp[idx-1]+1)
print(dp[dest])