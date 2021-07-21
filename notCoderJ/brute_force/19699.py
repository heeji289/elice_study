from itertools import combinations
from math import sqrt, floor
import sys

input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
cows = list(map(int, input().split()))

'''
    방법 1. 조합을 이용한 풀이
    풀이 과정:
        n과 m의 범위가 9이하이므로 완전 탐색을 통해 문제를 해결할 수 있다고 생각했습니다.
        
        1. 주어진 n마리의 소 중 m마리를 선택하는 모든 경우의 수를 구합니다.
        2. 1번의 각 케이스마다 소들의 무게 합을 구하고 소수인지 판별합니다.
            2-1. 소수를 판별하는 함수를 재귀함수로 구현했습니다.(어떤 수의 약수는 제곱근을 기준으로 대칭되므로 이를 이용했습니다.)
        3. 2번에서 구한 소수가 없는 경우 -1, 있는 경우 오름차순으로 출력합니다.
        
        여기서, answer를 집합으로 구현한 것은 중복되는 무게가 있을 수 있기 때문입니다.
'''
chkPrime = lambda x, y: x if y < 2 else None if not x % y else chkPrime(x, y - 1)
isPrime = lambda x: chkPrime(x, floor(sqrt(x))) 
answer = sorted({isPrime(sum(pack)) for pack in combinations(cows, m)} - {None})
print(*answer) if answer else print(-1)


'''
    방법 2: 재귀함수를 이용한 풀이
    풀이 과정:
        너무 조합으로만 푸는 느낌이 들어
        희지님이 사용하셨던 '선택 vs 미선택' 방식을 채용해서 재귀로 구현해봤습니다.
        다음에는 정규님이 사용하시던 '재귀 + for'도 도전해보겠습니다.
        
        1. 선택해야할 소의 수, 현재 선택 가능한 소의 수, 현재 무게의 합을 입력받는 재귀 함수를 수행합니다.
        2. 현재 해당하는 번째의 소를 선택하는 경우와 선택하지 않는 경우에 대해 다음과 같이 값을 갱신하여 1번을 반복 수행합니다.
            선택한 경우 : 선택해야할 소의 수 - 1, 현재 선택 가능한 소의 수 - 1, 현재 무게 + 현재 선택한 소의 무게
            선택하지 않은 경우 : 선택해야할 소의 수, 현재 선택 가능한 소의 수 - 1, 현재 무게
        3. 선택해야할 소의 수가 0인 경우 소수인지 검사해서 answer에 넣어주고 현재 선택 가능한 소의 수가 없는 경우 return을 수행합니다.
        4. answer에 수가 존재하면 해당 수들을 오름차순으로 출력하고 없으면 -1을 출력합니다.
    
'''
# answer = set()
# isPrime = lambda x, y: {x} if y < 2 else set() if not x % y else isPrime(x, y - 1)

# def selectCows(select, remain, weight):
#     global answer

#     if not select:
#         answer |= isPrime(weight, floor(sqrt(weight)))
#         return
#     elif not remain:
#         return
    
#     selectCows(select - 1, remain - 1, weight + cows[remain - 1])
#     selectCows(select, remain - 1, weight)    

# selectCows(m, n, 0)

# print(*sorted(answer)) if answer else print(-1)

