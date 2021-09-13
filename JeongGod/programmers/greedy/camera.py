def solution(routes):
    '''
    첫번째로 나간 차의 진출 지점을 먼저 카메라로 잡는다.
    1. 그 다음차의 진출 시점을 확인한다.
        1-1 그 다음차의 진출 시점이 현재 진출 시점보다 작거나 같다면
            그 곳이 최적의 카메라 위치다. 변경
        1-2 크다면
            그 차의 진입 시점을 확인한다.
            반복문을 통해 진입 시점이 현재 카메라 위치보다 작거나 같다면 점프
            아니라면 새로운 카메라를 설치한다.
    '''
    answer = 1
    routes.sort(key=lambda x: x[0])
    out = routes[0][1]
    for car in routes:
        new_in, new_out = car
        # 최적의 카메라 위치 변경
        if new_out <= out :
            out = new_out
            continue
        # 진입 시점을 확인한다.
        if new_in <= out:
            continue
        # 위를 만족하지 않는다면
        out = new_out
        answer += 1
            
        
    return answer
