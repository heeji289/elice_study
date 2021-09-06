# 히오스 프로게이머

"""
N개의 캐릭터 - 레벨은 X(i)
성권 -> 게임 끝날때까지 레벨을 최대 K만큼 올릴 수 있음

팀 목표레벨 T = min(X(i))
성권쓰가 달성할 수 있는 최대 팀 목표 레벨 T는?
"""
import sys
input = sys.stdin.readline

# n캐릭터 개수, k 올릴수 있는 레벨
n, k = map(int, input().split())

# 각 캐릭터의 레벨 N줄
levels = [int(input()) for _ in range(n)]
levels.sort()

left = min(levels)  # 현재 최소레벨
right = max(levels) + k  # 올릴 수 있는 최대 레벨

answer = 0

while left <= right:
    mid = (left + right) // 2  # 일단
    total = 0

    for level in levels:
        # 더 안찾아도 되니까
        if level >= mid:
            break
        # mid레벨이 되려면 총합 얼마의 레벨을 올려야 하는지 체크
        total += (mid - level)

    # 불가넝
    if total > k:
        right = mid - 1
    else:
        answer = mid  # 일단 값을 갱신
        left = mid + 1

print(answer)

