def solution(play_time, adv_time, logs):
    """
    1. 초마다 시청자 수가 몇 명이 있는지 센다.
    2. 시청자의 수는 곧 해당 초에 광고를 삽입했을 때 보여지는 초와 같다.
    3. 0~play_time까지 adv_time만큼 sum을 하여 그의 합이 가장 큰 값을 시작 시간으로 둔다.
    """
    def time_to_seconds(t):
        h, m, s = t.split(":")
        return int(h)*60**2 + int(m)*60 + int(s)

    def seconds_to_time(t):
        h = t // 3600
        t %= 3600
        m = t // 60
        t %= 60
        s = t
        return f"{h:0>2}:{m:0>2}:{s:0>2}"

    # 모두 초단위로 변경한다.
    play_time = time_to_seconds(play_time)
    adv_time = time_to_seconds(adv_time)
    viewer = [0] * (play_time+2)

    for l in logs:
        start, end = list(map(lambda x: time_to_seconds(x), l.split("-")))
        # start에서 viewer가 추가되고, end에서는 viewer가 빠져나간다.
        viewer[start] += 1
        viewer[end] -= 1

    # adv_time까지의 합을 구한다.
    adv_time_sum = 0
    cur = 0
    for i in range(adv_time):
        """
        1. viewer[i] < 0
            => 시청자가 빠져나간 것이다.
        2. viewer[i] > 0
            => 시청자가 추가 되었다는 뜻이다.
        """
        if viewer[i] > 0:
            cur += viewer[i]
        elif viewer[i] < 0:
            cur = cur + viewer[i] if cur + viewer[i] >= 0 else 0
        adv_time_sum += cur

    max_time = adv_time_sum
    answer = 0
    """
    구간합을 사용한다.
    1. 처음 합을 구한다. (위에 adv_time_sum)
    2. 한 칸씩 전진하면서 adv_time_sum에서 왼쪽 값은 빼주고, 오른쪽 값은 더해준다.
    3. 그러면 O(n)으로 구간합을 구할 수 있다.
    """
    for left in range(play_time-adv_time):
        right = left + adv_time
        # left, right에서 추가된 viewer가 있는지 검사한다.
        cur += viewer[right] - viewer[left]
        adv_time_sum += cur
        if adv_time_sum > max_time:
            max_time = adv_time_sum
            answer = left + 1
    return seconds_to_time(answer)
