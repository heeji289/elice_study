"""
참고: https://deok2kim.tistory.com/122
뭐를 찾는다고 생각해야할지..

우리는 주어진 바위 중에 n개를 제거할 건데 바위간 거리 최솟값 중에 가장 큰 값을 구할 것임
돌과 돌 사이를 target으로 둔다고 할 거임 바위를 제거해나갔을 때 target보다 거리가 짧으면 돌을 제거하고 아니면 그 돌로 이동
이런 식으로 돌을 제거하고 그 거리를 구했을 때 그 최소값이 target값과 일치하는 걸 찾아야한다
"""

def solution(distance, rocks, n):
    answer = 0
    
    start, end = 1, distance
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2 # target: 돌 사이 거리의 최솟값
        
        current_rocks = 0 # 현재 우리가 보고 있는 돌의 위치
        deleted_rocks = 0 # 제거한 돌의 수
        min_distance = 1e7
        
        for rock in rocks:
            # 돌 사이 거리가 mid보다 작으면 돌을 제거
            if rock - current_rocks < mid:
                deleted_rocks += 1
            # 그렇지 않으면 최소거리를 갱신하고 바위 위치를 옮긴다
            else:
                min_distance = min(min_distance, rock - current_rocks)
                current_rocks = rock
                
        if deleted_rocks > n:
            end = mid - 1
        else:
            answer = min_distance
            start = mid + 1
    
    return answer