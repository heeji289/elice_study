def solution(distance, rocks, n):
    """
    가능한 거리를 이분탐색으로 찾는다.
    1. 삭제한 돌이 n개 초과라면
        해당 거리보다 작은 친구들이 너무 많다는 얘기다. => 즉 해당 거리로 이루어지게 징검다리를 구성할 수 없다는 얘기
        그렇다면 거리를 줄여서 n개 이하로 만들어보자.
    2. 삭제한 돌이 n개 이하라면
        해당 거리는 가능하다는 얘기다. 
        하지만, 지금 선택한 거리보다 더 크게 해도 가능할 수도 있다.
        그렇기 때문에 거리를 더 크게 늘려본다.
    """
    answer = 0
    # 처음 시작점과 끝점을 가져온다.
    rocks.append(0); rocks.append(distance)
    rocks.sort()
    left, right = 0, rocks[-1]
    while left <= right:        
        mid = (left + right) // 2

        ############# 1. 기존 풀이
        cnt, tmp_dist = 0, 0
        tmp_cnt = 1
        # 해당 mid값(내가 지금 선택한 거)과 비교한다.
        for idx in range(1, len(rocks)):
            # 쓸데없는 계산을 위해 나온다.
            if cnt > n:
                break

            tmp_dist += rocks[idx] - rocks[idx-1]
            # 돌의 거리가 아직 기준(mid)보다 만족하지 못 한다면 돌을 더 없애야 한다는 얘기
            if tmp_dist <= mid:
                tmp_cnt += 1
            # 지금까지 더한 돌의 거리가 기준(mid)보다 크기때문에 mid에 만족하는 거리 => 돌을 없애지 않아도 된다는 얘기다.
            else:
                cnt += tmp_cnt-1
                tmp_cnt, tmp_dist = 1, 0
        cnt += tmp_cnt - 1

        # 이제 cnt값과 n값을 비교한다.
        if cnt > n:
            right = mid-1
        else:
            left = mid+1
    return left



def solution(distance, rocks, n):
    answer = 0
    # 처음 시작점과 끝점을 가져온다.
    rocks.append(0); rocks.append(distance)
    rocks.sort()
    left, right = 0, rocks[-1]
    while left <= right:        
        mid = (left + right) // 2

        ############# 2. 다른 사람의 풀이를 참고하여 더 깔끔하게 만든 풀이
        cnt, tmp = 0, rocks[0]
        # 해당 mid값(내가 지금 선택한 거)과 비교한다.
        for idx in range(1, len(rocks)):
            # 쓸데없는 계산을 위해 나온다.
            if cnt > n:
                break
            # 돌의 거리가 기준(mid)에 만족하지 않는다면 없앤다.
            if rocks[idx] - tmp <= mid:
                cnt += 1
            # 돌의 거리가 기준(mid)보다 크기때문에 mid에 만족하는 거리
            else:
                tmp = rocks[idx]

        # 이제 cnt값과 n값을 비교한다.
        if cnt > n:
            right = mid-1
        else:
            left = mid+1
    return left
