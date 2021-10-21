def solution(n, t, m, timetable):
    """
    제일 늦은 도착 시각을 출력해야한다.

    1. queue에 사람들을 시간순으로 담는다.
    2. queue에 맨 앞에 있는 사람이 셔틀에 탈 수 있으면 태운다.
    3. 콘이 탈 수 있는 셔틀의 시간을 업데이트한다.
        => 해당 시간 셔틀이 꽉 찼다면 마지막 탄 사람의 -1
        => 셔틀이 꽉 차지 않았다면 해당 셔틀 시간
    """
    # 크루들을 시간대로 정렬
    def hour_to_min(x):
        hour, minute = map(int, x.split(":"))
        return hour*60 + minute
    crews = sorted(map(lambda x: hour_to_min(x), timetable), reverse=True)

    start = 540  # 09:00 첫 셔틀 시간
    end = start + t*(n-1)  # 마지막 셔틀 시간
    ans = 0
    # 셔틀시간대 별로 사람들을 태운다.
    for bus_time in range(start, end+1, t):
        bus_person = 0
        while True:
            # 셔틀이 꽉 찼거나, 태울 사람이 없거나, 시간에 맞지 않은 사람이라면 패스
            if bus_person == m or len(crews) == 0 or crews[-1] > bus_time:
                break
            bus_person += 1
            last_person = crews.pop()
        # 탈 수 있는 셔틀의 시간을 업데이트 한다.
        if bus_person == m:
            ans = last_person - 1
        else:
            ans = bus_time

    # 출력 형식에 맞게 변형
    hour, minute = divmod(ans, 60)
    ans_hour = "0" + str(hour)
    ans_minute = "0" + str(minute)

    return ans_hour[-2:] + ":" + ans_minute[-2:]
