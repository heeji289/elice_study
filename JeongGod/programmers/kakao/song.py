def solution(m, musicinfos):
    '''
    한 음악 반복 재생 가능
    네오가 기억하고 있는 멜로디는 음악 끝 -> 처음 부분이 이어서 재생된 멜로디일 수도 있다.
    한 음악을 중간에 끊을 경우 => 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.
    네오가 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하자.
    
    각 음은 1분에 1개씩 재생 (반드시 처음부터 재생 => (재생된 시간 > 음악 길이)라면 => 반복 재생이다.)
    조건이 일치하는 음악이 여러 개 => 재생된 시간이 제일 긴 음악 제목을 반환 => 먼저 입력된 음악 제목 반환
    '''
    answer = []
    
    def hour_to_minute(t):
        h, m = t.split(":")
        return int(h)*60 + int(m)
    
    for music in musicinfos:
        start, end, title, info = music.split(",")
        during = hour_to_minute(end) - hour_to_minute(start)
        
        # info를 악보별로 list화 한다.
        info_list = []
        for i in info.split("#"):
            info_list += [j for j in i]
            info_list[-1] += "#"
        # 마지막에 "#"을 제거한다.
        info_list[-1] = info_list[-1][:-1]

        tmp = ""
        # 재생되는 시간과 멜로디 길이 확인
        if during <= len(info_list):
            tmp += "".join(info_list[:during])
        # 재생되는 시간이 길면 계속 더해준다.
        else:
            for idx in range(0, during+1, len(info_list)):
                tmp += "".join(info_list[:during-idx])

        # 현재 멜로디 안에 m이 들어있는지 확인
        start = 0
        while True:
            s_idx = tmp.find(m, start)
            end_idx = s_idx+len(m)
            # 찾지 못했다면
            if s_idx == -1 :
                break
            # m이 있다는 것을 찾았지만 "#"이 붙어서 일치하지 않는거라면
            if end_idx < len(tmp) and tmp[end_idx] == "#":
                start += len(m)
                continue
            answer.append((title, during))
            break

    
    return sorted(answer, key=lambda x: x[1], reverse=True)[0][0] if len(answer) != 0 else "(None)"
