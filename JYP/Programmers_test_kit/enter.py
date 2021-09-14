def solution(n, times):
    times.sort()
    start = 1
    end = times[-1] * n # maximum

    while start < end:
        mid = (start + end) // 2
        cnt = 0

        for time in times:
            cnt += mid // time

        if cnt < n:
            start = mid + 1
        else:
            end = mid

        answer = start
    
    return answer