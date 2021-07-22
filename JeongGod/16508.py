'''
1. target counter dict를 생성한다.
2. title에 대한 counter dict를 생성한다.
3. title에 대한 조합을 만든다.
4. title에 대한 조합중에서 target_dict.keys()를 하나씩 돌아봅니다.(해당 title에서 뽑을 수 있는지 없는지 판단)
5. 만약 가능한 조합이라면, 해당 조합의 가격을 더해 최소값이랑 비교합니다.
'''
import sys, math
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

def find(com, targets):
    # 조합들의 알파벳 개수와 가격을 합친다.
    tmp = Counter()
    result = 0
    for elem in com:
        tmp.update(elem[0])
        result += elem[1]
    # 합친 알파벳 개수와 target의 알파벳 개수를 비교한다.
    flag = True
    for key, val in targets.items():
        cnt = tmp.get(key, 0)
        if cnt < val:
            flag = False
            break
            
    # 가능한 조합이라면 가격을 리턴한다.
    return result if flag else math.inf


targets = Counter(input().rstrip())

n = int(input())

books = []
for i in range(n):
    val, title = map(str, input().rstrip().split())
    books.append((Counter(title), int(val)))

ans = math.inf
for i in range(1,len(targets)+1):
    for com in combinations(books, i):
        ans = min(ans, find(com, targets))

print(ans if ans != math.inf else -1)
