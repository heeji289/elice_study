# [고득점 KIT 그리디] 단속카메라

"""
차량의 경로를 보고 모든 차량이 한 번은 카메라를 만나도록 설치

[처음 생각]
1. 이동경로가 제일 작은 차량이 나가는 지점에 카메라 설치
 - 해당 카메라로 단속할 수 있는 차량들 모두 체크
2. 반복..

[틀린 부분]
- 정렬할 때 이동경로가 제일 작은 애를 기준으로 한 것.
- 참고 : https://programmers.co.kr/questions/14636

"""

def solution(routes):
    answer = 0
    
    # 이동경로가 짧은 순 & 나가는 지점이 더 빠른 순으로 정렬
    # => 그냥 나가는 지점이 더 빠른 순 정렬
    
    # routes.sort(key=lambda x: (x[1] - x[0], x[1]))
    routes.sort(key=lambda x: x[1])
    visited = [False] * len(routes)
    
    for i in range(len(routes)):
        if not visited[i]:
            visited[i] = True
            new_camera = routes[i][1] # 나가는 지점에 카메라
            answer += 1
        for j in range(i + 1, len(routes)):
            if visited[j]: continue # 예외처리
            if routes[j][0] <= new_camera <= routes[j][1]:
                visited[j] = True
    
    return answer