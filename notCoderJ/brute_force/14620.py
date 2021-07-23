'''
    풀이 요약:
        처음에는 재귀로 시도해보려고 한참을 헤매이다가 저주받을 꽃잎때문에 포기...
        다른 관점에서 문제를 파악해야겠다고 생각해서 그림판으로 열심히 색칠공부하다가...
        꽃의 중점 간 거리가 3이상이어야 한다는 걸 발견하고 유레카를 외친 후 열심히 조합으로 풀었습니다.
        
        1. 2차원 화단의 모든 좌표를 구한 후 3개의 좌표쌍을 모두 구합니다.
        2. 1번에서 구한 좌표쌍에서 각 좌표 간 거리가 3이상인지 확인합니다.
        3. 모든 거리가 3이상이라면 해당 좌표들에서 가격을 구한 후 answer와 비교해 작은 값을 answer로 취합니다.
'''

from itertools import combinations, product
import sys
input = lambda: sys.stdin.readline().rstrip()


answer = 3001
n = int(input())
locations = product(range(1, n - 1), repeat=2)
costs = [list(map(int, input().split())) for _ in range(n)]

# 두 점 사이의 거리를 구하는 함수 / 입력: 2차원 튜플 ((a, b), (c, d)) / 출력: 두 점 사이 간격
dist = lambda x: abs(x[0][0] - x[1][0]) + abs(x[0][1] - x[1][1])
# 현재 식물의 차지한 공간(현재 위치, 상, 하, 좌, 우)에 대한 가격을 구하는 함수
# 입력: 2차원 튜플 ((a, b), (c, d)) / 출력: 두 점 사이 간격
cost = lambda x: costs[x[0]][x[1]] \
                + costs[x[0] - 1][x[1]] \
                + costs[x[0] + 1][x[1]] \
                + costs[x[0]][x[1] - 1] \
                + costs[x[0]][x[1] + 1]

for plant in combinations(locations, 3):
    a, b, c = map(dist, combinations(plant, 2))
    if all([a > 2, b > 2, c > 2]):
        answer = min(answer, sum(map(cost, plant)))

print(answer)

'''
    아래는 위 코드를 풀어서 해석한 코드입니다.
    뭔가 하도 줄여쓰다보니... 풀어 쓰려니 좀 헤깔리네요 ㅎㅎ
    허허 풀어쓴 풀이가 속도는 2배가량 빠르네요;;
'''
'''
costs = []
for _ in range(n):
    line = list(map(int, input().split()))
    costs.append(line)

# 두 점 사이의 거리를 구하는 함수 / 입력: 튜플 a: (x1, y1), b: (x2, y2)) / 출력: 두 점 사이 간격
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 현재 식물의 차지한 공간(현재 위치, 상, 하, 좌, 우)에 대한 가격을 구하는 함수
# 입력: 2차원 튜플 ((a, b), (c, d)) / 출력: 두 점 사이 간격
def cost(x, y):
    up = costs[x - 1][y]
    down = costs[x + 1][y]
    left = costs[x][y - 1]
    right = costs[x][y + 1]
    return costs[x][y] + up + down + left + right

for plant in combinations(locations, 3):
    cnt = 0
    for a, b in combinations(plant, 2):
        d = dist(a, b)
        if d > 2:
            cnt += 1
    if cnt == 3:
        total = 0
        for x, y in plant:
            total += cost(x, y)
        answer = min(answer, total)

print(answer)
'''