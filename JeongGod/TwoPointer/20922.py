'''
N = 200,000
M = 100
memory 1024MB
1 second

left, right잡는다. left = 0, right = 1
right를 한 칸씩 옮기면서 개수를 센다. 개수는 defaultdict로 세자.
그러다가 _dict[_li[right]] > k 가 된다면 _li[right]와 같은 숫자였던 처음 위치를 찾는다.
left = (그 위치+1)로 삼고 right는 계속 옆으로 간다.
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())

_li = list(map(int, input().split()))
_dict = defaultdict(list)
left = 0
ans = 0
for right in range(N):
    # 현재 숫자
    num = _li[right]
    # key = 숫자, value = [index1, index2 ... ]
    _dict[num].append(right)
    
    if len(_dict[num]) > K :
        # 겹치는 친구의 index가 지금 left보다 작다면 지금 순열에 포함되지 않은 친구이다. pop해주고 넘어간다.
        if _dict[num][0] < left:
            _dict[num].pop(0)
            continue
        ans = max(ans, right-left)
        left = _dict[num][0]+1
        _dict[num].pop(0)
print(max(ans, (right+1)-left))
