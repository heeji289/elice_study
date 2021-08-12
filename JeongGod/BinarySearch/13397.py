'''
N = 5000, M = 5000
최대 5000개를 포함한 배열을 만들 수 있다. 이 중 (최대 - 최소)의 값이 "최소"가 되게 만들어보자.

임의로 만든 최솟값(tmp)을 생각해본다. (0 + 10000) // 2
이 tmp값이 지금 구간으로 나눠보면 어떻게 되는지 판단해본다.
1. 만약 구간으로 나눈 개수가 M보다 크다면
    => 우리가 생각한 tmp값을 좀 더 늘려도 되겠다. 구간의 개수를 줄여야 답으로 인정받을 수 있으니깐.
2. 만약 구간으로 나눈 개수가 M보다 작거나 같다면
    => 조건에 부합하니 해당 tmp값을 임시로 답으로 지정해놓자.
    그리고 tmp의 값이 더 작아도 이 조건에 부합하는지 판단해보자.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_li = list(map(int, input().split()))

left, right = 0, 10001
result = 0
# 우리가 (최대-최소)의 최댓값 tmp값을 임시로 정해보자.
while left <= right:
    tmp = (left+right) // 2
    cnt = 1
    min_val, max_val = sys.maxsize, -1

    # tmp값으로 설정했을 경우 몇 개의 구간으로 나뉘어지는지 확인해보자.
    for i in range(N):
        max_val = max(max_val, _li[i])
        min_val = min(min_val, _li[i])
        # 해당 구간의(최대-최소)가 tmp보다 크다면 구간을 나눈다.
        if max_val - min_val > tmp:
            cnt += 1
            min_val = _li[i]
            max_val = _li[i]

    '''
    덜 쪼개지거나 같다면(cnt <= M)
        가능한 경우다. 임시로 답을 지정해놓는다.
        하지만 아직 더 볼 수 있는 경우가 있다. 우리는 "최소값"을 찾아야 한다.
        그래서 tmp보다 작은 경우를 탐색한다.
    많이 쪼개진다면
        가능하지 않은 경우다. tmp가 너무 작다는 얘기다.
        그래서 tmp의 값을 올려서 덜 쪼개지는 방향으로 탐색해야한다.
    '''

    if cnt <= M:
        result = tmp
        right = tmp-1
    else:
        left = tmp+1
print(result)