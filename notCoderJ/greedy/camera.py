'''
  풀이 요약
    차량들을 나간 지점을 기준으로 정렬한 뒤 현재 차량의 나간 지점과 이전 차량의 진입 지점을 비교하여
    현재 차량의 나간 지점 < 이전 차량의 진입 지점이면 현재 차량의 진입 지점에 카메라를 1대 추가하고 카메라의 설치 위치를 갱신합니다.
    현재 차량의 나간 지점 > 이전 차량의 진입 지점인 경우 이전 차량의 진입 지점과 현재 차량의 진입 지점을 비교하여 더 큰 값으로 카메라의 위치를 갱신해줍니다.
    실제 풀이는 위 로직을 사용했으나 정렬만 역순으로 하여 진행했습니다.
    
    예를 들어 현재 차량 = (5, 7), 이전 차량 = (3, 9)라면
    현재 차량의 나간 지점(7) > 이전 차량의 진입 지점(5)이므로
    카메라를 추가하지 않고 카메라의 설치 위치만 둘의 진입 지점 중 더 큰 값(5)로 갱신합니다.
'''

# 다시 푼 풀이
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: -x[1])
    
    camera = 30001
    for s, e in routes:
        if e < camera:
            answer += 1
            camera = s
        elif s > camera:
            camera = s
    return answer


# 이전 풀이
def solution(routes):
    answer = 0
    routes.sort(reverse=True)
    
    camera = 30001
    for s, e in routes:
        if e < camera:
            answer += 1
            camera = s
    return answer