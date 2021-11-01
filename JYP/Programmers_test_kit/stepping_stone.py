'''
풀이1 - 바위의 거리를 대상으로 이진탐색
1. 바위들을 위치 순으로 정렬
2. mid보다 현재 바위 간 거리가 짧으면 지금 바위를 제거 : cnt += 1
3. cnt가 제거 가능한 바위 개수 n값보다 크다면 mid 증가
4. cnt가 n값보다 작다면 mid 감소
5. 카운트하는 동안 저장한 거리의 최솟값 반환하기
'''
def solution(distance, rocks, n):
    # # 0. 예외처리 - 바위의 개수 == 제거할 바위 개수 n이면 전체 거리를 바로 반환
    # if len(rocks) == n:
    #     return distance

    # 1. 바위를 위치 순으로 정렬한다.
    rocks.sort()

    total_cnt = len(rocks)
    start = 1
    end = distance
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        prev_rock = 0
        cnt = 0
        min_dist = 1e10

        # 2. 현재 바위 간 mid 이하라면 바위를 제거 : cnt += 1
        for curr_rock in rocks[:total_cnt]:
            curr_dist = curr_rock - prev_rock
            if curr_dist < mid:
                cnt += 1
                if cnt > n : # 제거할 수 있는 바위 개수를 초과한다면 for문 중단
                    break
            else:
                min_dist = min(min_dist, curr_dist) # 최솟값 찾기
                prev_rock = curr_rock
        
        # 3. 추가 처리 - 마지막 바위와 도착지점 간 거리를 mid와 비교
        if rocks[-1] - rocks[-2] < mid and distance - rocks[-1] < mid:
            cnt += 1
            min_dist = min(min_dist, rocks[-1] - rocks[-2], distance-rocks[-1]) # 최솟값 찾기
        
        # 4. 지금까지 제거한 바위의 수cnt > 제거 가능한 바위 수 최댓값 n이면
        # mid 감소시키기
        if cnt > n :
            end = mid - 1

        # 5. cnt가 n보다 작거나 같으면
        # mid 증가시키기
        # 이 때의 min_dist 값은 답안에 저장
        else:
            answer = min_dist
            start = mid + 1
       
    
    return answer

'''
풀이2 - 당연하게도 런타임 에러
1. 바위들을 위치 순으로 정렬한다
2. 거리 값이 최소인 바위 2개를 제거한다.
3. 남은 바위 간 거리의 최솟값을 반환한다.
'''
'''
from collections import deque

def solution(distance, rocks, n):
    answer = 0

    # 1. 바위를 위치 순으로 정렬한다.
    rocks = sorted(rocks)

    # 예외처리? 바위의 개수와 제거할 바위 개수가 같으면 전체 거리를 바로 반환
    if len(rocks) == n:
        return distance
    

    # 2. 거리 값이 최소한 바위 찾기
    def make_distances(rocks):
        distances = []
        
        for i in range(len(rocks)+1):
            if i == 0:
                dist = rocks[i]
            elif i == len(rocks):
                dist = distance - rocks[i-1]
            else:
                dist = rocks[i] - rocks[i-1]
            
            insort(distances, [dist, i])
        return distances
    
    
    # 3. 바위 n개 제거하기
    distances = make_distances(rocks)
    rocks = deque(rocks)
    for i in range(n):
        idx = distances[i][1] if distances[i][1] != 0 else 1
        remove_idx = idx - 1
        rocks.remove(rocks[remove_idx])

    # 4. 거리의 최솟값 중 최댓값 찾기
    distances_removed = make_distances(rocks)
    answer = distances_removed[0][0]
    return answer


'''


'''
TEST CASES
'''
'''
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
# return 4

# distance = 23
# rocks = [3, 6, 9, 10, 14, 17]
# n = 2
# # return 3

# distance = 10
# rocks = [3, 5, 7]
# n = 2
# # return 5

print(solution(distance, rocks, n))
'''
