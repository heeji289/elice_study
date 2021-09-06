# 숫자 카드

"""
상근이 : 숫자 카드 N개
정수 M개가 주어졌을 때, 상근이가 해당 수가 적혀있는 카드를 갖고있는지 아닌지

1. 상근이 카드를 정렬한다
2. 이진탐색 함수 (left, right, target)
    - 중간값 = left + right / 2
    - 만약 중간값 == target -> return True
    -            > target -> right = mid - 1
    -            < target -> left = mid + 1
"""

import sys
input = sys.stdin.readline

# N 숫자카드 개수
n = int(input())
# N개의 숫자들 (상근쓰 카드)
cards = list(map(int, input().split()))
# M 찾을? 개수
m = int(input())
# M개의 숫자들 (찾을 것들) -> 각각에 대해 갖고 있으면 1, 아니면 0을 
search_cards = list(map(int, input().split()))

# 정렬..
cards.sort()

def binary_search(left, right, target):
    while left <= right:
        mid_idx = (left + right) // 2
        mid = cards[mid_idx]

        if mid == target: return 1
        elif mid < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
        
    return 0

for item in search_cards:
    print(binary_search(0, n - 1, item), end = ' ')


