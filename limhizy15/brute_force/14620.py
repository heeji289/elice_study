# 꽃길

"""
[문제]
주어진 화단에 씨앗 3개를 심으려 한다.
씨앗은 1년 뒤 꽃이 피며 상하좌우에 꽃잎이 생긴다.
이 꽃들은 다른 꽃의 꽃잎 혹은 꽃술과 닿게 되면 죽는다. 화단밖으로 벗어나서 자라도 죽는다.
꽃들이 죽지 않게 3개의 꽃이 다 피도록 씨앗을 심고 싶다.
& 싼 값에 화단을 대여하고 싶다. (3개의 꽃이 필 공간 : 15평)

[풀이]
1. 화단의 모든 좌표 중 3곳을 선택한다.
2. 이 3곳이 정상적으로 꽃이 필 수 있는 위치인지 확인한다.
    1) flower = {}  근데 딕셔너리 키 값으로 튜플이나 리스트가 가능한가? 안된대 그냥 배열로
    2) 네 방향을 탐색해서 이미 flower에 있는 위치인지 확인하고
        - 아직 꽃이 피지 않은 위치라면 flower에 추가, 비용도 추가!
        - 꽃이 피었다면 이 경우에 정상적으로 꽃이 필 수 없다. return으로 종료
    3) 가능한 경우 비용의 최솟값을 갱신해준다.

*** 풀이는 떠올랐으나 구현을 어떻게 할 지 모르겠어서 블로그들을 참고했습니다.
*** 파이썬에서 pair를 어떻게 저장할지 모르겠어서.. C++때는 pair<int, int> 이렇게했었는데..
"""

import sys
from itertools import combinations

input = sys.stdin.readline

answer = int(1e9)

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solve(arr):
    global answer

    flower = []
    money = 0

    # 세 개의 좌표를 탐색
    for y, x in arr:
        flower.append((y, x))  # 일단 씨앗의 위치에 꽃이 핌
        money += prices[y][x]
        # 상하좌우에 꽃이 필 수 있는지 확인
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 이미 해당 위치에 꽃이 폈다.
            if ((ny, nx) in flower):
                return
            # 화단 밖으로 꽃이 핀다.
            if ny < 0 or ny >= n or nx < 0  or nx >= n:
                return
            else:
                flower.append((ny, nx))
                money += prices[ny][nx]
    
    # 화단 비용 최솟값 갱신
    answer = min(answer, money)


# 화단 한 변의 길이 입력
n = int(input())
# 화단 가격 입력
prices = [list(map(int, input().split())) for _ in range(n)]

# 화단의 모든 좌표를 배열에 저장 (y, x) 형태로 ***pair는 튜플로 해결하자!
possible = [(y, x) for x in range(0, n) for y in range(n)]

for arr in combinations(possible, 3):
    solve(arr)

print(answer)
