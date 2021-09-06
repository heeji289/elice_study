# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

'''
아이스크림 가게 : N종류 아이스크림 (1~N번)
같이 먹으면 안좋은 조합이 있음
이런 경우를 피해서 아이스크림을 3가지 선택하려한다.

생각)
1. 세개로 만들 수 있는 조합을 모두 구한다.
2. 조합안에 안좋은 조합이 섞여있는지 확인한다.
3. 나머지 경우를 구한다.
'''

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
worst = {}  # 조합을 문자열로 저장
ice = []

for i in range(n):
    ice.append(i+1)

# x번 - y번 연결
for _ in range(m):
    x, y = map(int, input().split())
    tmp = ""
    tmp += str(x) + "&" + str(y)
    worst[tmp] = True

    tmp = ""
    tmp += str(y) + "&" + str(x)
    worst[tmp] = True

answer = 0

for comb in combinations(ice, 3):
    flag = True
    for find_worst in combinations(comb, 2):
        f = ""
        f += str(find_worst[0]) + "&" + str(find_worst[1])
        f2 = ""
        f2 += str(find_worst[1]) + "&" + str(find_worst[0])
        if f in worst.keys() or f2 in worst.keys():
            flag = False
            break
    if flag:
        answer += 1

print(answer)