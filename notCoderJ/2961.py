'''
    풀이 과정:
        재료의 갯수가 최대 10개이므로 모든 재료의 조합을 구하여 계산해도 되겠다고 생각.
        1. 반복적인 재료의 조합에 대한 연산을 줄이기 위해 메모이제이션을 이용함(신맛, 쓴맛을 담는 딕셔너리를 정의)
        2. 재료의 개수를 1 ~ n개까지 선택하는 조합을 구하고 각 조합에서 memo 테이블을 참조하여 현재 조합의 신맛과 쓴맛을 구한다.
        3. 2번에서 구한 신맛과 쓴맛을 memo 테이블에 저장하고 두 맛의 차이를 계산하여 기존 맛의 차이와 비교 후 더 작은 값으로 맛의 차이 값을 갱신한다.
'''

from itertools import combinations


diff = float("inf")

n = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]
memo = {(): [1, 0]} # [신맛, 쓴맛]

for i in range(1, n + 1):
    for j in combinations(range(n), i):
        sour = memo[j[:-1]][0] * ingredients[j[-1]][0]
        bitter = memo[j[:-1]][1] + ingredients[j[-1]][1]
        memo[j] = [sour, bitter]
        diff = min(diff, abs(sour - bitter))
        
print(diff)