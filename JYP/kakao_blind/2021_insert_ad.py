import heapq


def convert_sec(time):

    hour, min, sec = list(map(int, time.split(':')))
    seconds = hour * 3600 + min * 60 + sec

    return seconds

def convert_hhmmss(sec):
    h, m = divmod(sec, 3600)
    m, s = divmod(m, 60)
    
    hhmmss = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
    return hhmmss



def solution(play_time, adv_time, logs):
    answer = ''

    if play_time == adv_time:
        return '00:00:00'

    in_out = []
    
    for log in logs:
        start, end = log.split('-')
        start_sec = convert_sec(start)
        end_sec = convert_sec(end)
        heapq.heappush(in_out, (start_sec, 1))
        heapq.heappush(in_out, (end_sec, -1))

    time_logs = []
    acc_user = 0

    while in_out:
        time, cnt = heapq.heappop(in_out)
        acc_user += cnt
        time_logs.append([time, acc_user])

    
    adv_sec = convert_sec(adv_time)
    end_idx = 1
    acc_user = 0
    acc_time = 0
    max_acc_time = 0
    

    for start, acc_user in time_logs:
        acc_time = 0
        length = 0

        while length < adv_sec:  
            end_idx += 1
            if end_idx > len(time_logs) - 1:
                break
            end = time_logs[end_idx][0]
            before_end = time_logs[end_idx-1][0]
            user_cnt = time_logs[end_idx-1][1]
            interval = end - before_end
            acc_time += interval * user_cnt
            length = end - start
            
        if acc_time > max_acc_time:
            result_time = start
            max_acc_time = acc_time
        
    answer = convert_hhmmss(result_time)
    
    return answer

