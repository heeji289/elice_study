'''
  풀이요약
    1. 0부터 최대 가능한 거리 distance까지 이분 탐색을 반복 수행하며, 중간 값을 가능한 최대 거리라 가정합니다.
    2. 중간 값보다 간격이 적은 바위들을 하나씩 제거하며 제거한 바위 수가 n과 동일할 경우 answer를 중간값으로 변경해줍니다.
'''
def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.sort()
    
    while left <= right:
        mid = (left + right) // 2
        current, cnt = 0, 0
        
        for rock in rocks:
            if rock - current < mid:
                cnt += 1
            else:
                current = rock
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    
    return answer