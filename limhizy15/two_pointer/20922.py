# 겹치는 건 싫어

"""
도현쓰 : 수열에서 같은 원소가 여러 개 있는 게 싫어!
원소가 K개 이하로 들어있는 최장 연속 부분 수열의 길이를..

원소들의 개수를 세 면서 움직여~

end를 움직이며 k개 이하면 전진..
아니면 start를 전진.. 

디버깅하며 참고한 블로그 : https://khu98.tistory.com/187
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

# n, k 
n, k = map(int, input().split())
# 수열 정보 입력 
arr = list(map(int, input().split()))
# 원소의 개수를 저장
cnt = defaultdict(int)
# 각 각 수열의 시작, 끝을 가리킬 포인터
start, end = 0, 0
answer = 0

# 수열길이를 벗어나면 멈춤 
while end < n:
    # 현재 가리키고 있는 원소의 개수가 k 이하이면 
    if cnt[arr[end]] < k:
        # 원소 개수를 1 증가시키고
        cnt[arr[end]] += 1
        # end포인터를 전진시킴
        end += 1
    else:
        # start가 가리키는 원소를 1 감소시키고
        cnt[arr[start]] -= 1
        # start를 전진시킴
        start += 1
    
    # end - start와 answer 중 최대값을 선택
    answer = max(answer, end - start)

print(answer)
