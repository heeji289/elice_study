'''
    풀이 과정:
        주어진 N의 최댓값이 200이므로 N개에서 3개를 선택하는 조합의 수가 약 130만으로
        모든 경우의 수를 탐색해도 괜찮다고 생각했습니다.

        그래서 섞지 말아야할 아이스크림 조합에 대한 집합을 만들고, N개 중 3개의 아이스크림을
        선택하는 조합을 구해 하나씩 돌며 해당 집합과 교집합이 없는 경우만 카운트하여 아이스크림을 조합수를 구하겠다고 생각했습니다.
'''

from itertools import combinations
import sys

input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
# 이후 아이스크림 조합과 교집합 비교시 매칭되게 하기 위해 섞지 말아야할 각 아이스크림 조합을 오름차순으로 정렬했습니다.
not_mix = set(tuple(sorted(map(int, input().split()))) for _ in range(m)) 
# 각 아이스크림 조합에서 2개를 선택하는 조합을 집합으로 만들어 섞지 말아야할 아이스크림 조합과 교집합이 있는지 확인했습니다.
print(len([True for ice in combinations(range(1, n + 1), 3) if not set(combinations(ice, 2)) & not_mix]))