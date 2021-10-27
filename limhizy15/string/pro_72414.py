# 시청자들이 가장 많이 보는 구간에 광고를..
"""
참고 블로그 : https://dev-note-97.tistory.com/156
0으로 채우기 참고 : http://daplus.net/python-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%97%90-0%EC%9D%84-%EC%B1%84%EC%9A%B0%EB%8A%94-%EB%B0%A9%EB%B2%95/
"""

# "HH:MM:SS" 형태를 초 단위로 변환하는 함수
def str2sec(string):
    hour, minute, seconds = map(int, string.split(':'))
    return hour * 3600 + minute * 60 + seconds

# 초를 "HH:MM:SS"로 변환하는 함수
def sec2str(seconds):
    string = ''
    hour = seconds // 3600
    seconds -= hour * 3600
    
    minute = seconds // 60
    seconds -= minute * 60
    
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(seconds).zfill(2)}"
    

def solution(play_time, adv_time, logs):
    answer = 0
    
    # 시간을 초 단위로 변환
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)
    
    # 해당 시간에 보고 있는 사람들 수를 저장
    timeline = [0] * (play_time + 1)
    
    # logs를 돌면서 시작시간에 사람 수를 +1, 종료 시간에 -1
    for item in logs:
        # H1:M1:S1-H2:M2:S2 형식에서 초 단위로
        start, end = map(str2sec, item.split('-'))
        timeline[start] += 1
        timeline[end] -= 1
    
    # 앞에서 경계라인에서만 사람 수를 구했기 때문에.. 그 사이 값을 채운다
    for i in range(1, play_time + 1):
        timeline[i] = timeline[i] + timeline[i - 1]
    
    # 누적 시간을 구하기 위해 한 번 더.. => 어떤 구간에 시청자 수를 구하기 위해
    for i in range(1, play_time + 1):
        timeline[i] = timeline[i] + timeline[i - 1]
    
    max_cnt = timeline[adv_time] # 0초에 광고를 했을 때 사람 수

    for start in range(1, play_time):
        # 광고 종료 시간이 영상 재생시간을 넘어가면.. 
        # 광고 종료 시간을 영상 종료 시간으로 둔다..
        # 아니면 광고 시간만큼 더해서.. 광고 종료 시간을 결정..
        end = play_time if start + adv_time >= play_time else start + adv_time
        # 해당 구간에서 시청자수를 보고 갱신
        if max_cnt < timeline[end] - timeline[start]:
            max_cnt = timeline[end] - timeline[start]
            answer = start + 1
    
    return sec2str(answer)