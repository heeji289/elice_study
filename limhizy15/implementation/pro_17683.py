# 2018 kakao [3차] 방금그곡

'''
멜로디와 악보를 비교
1. 제목 / 재생 시작, 끝 시각 / 악보 정보제공
2. 음은 12개
3. 각 음은 1분에 1개씩 재생. 처음부터 재생, 반복재생
4. 조건이 일치하는 게 많으면 재생된 시간이 제일 긴 음악을 반환
 - 재생된 시간도 같으면 먼저 입력된 음악 제목을 반환
 - 조건 일치 없으면 None 반환

'''

def change(key):
    return key.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

# m : 네오 기억 / musicinfos : 방송된 곡의 정보
def solution(m, musicinfos):
    answer = ('(None)', 0) # 초기화 (0은 플레이시간)
    
    # #이 붙어있는 음들 치환 (검색한 부분 😤)
    m = change(m)
    
    for info in musicinfos:
        start, end, title, music = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        # 분 단위로 변환
        play_time = 60 * (end_h - start_h) + (end_m - start_m)
        
        music = change(music)
        # 반복재생이기 때문에 play_time을 곱해서 길이 늘려줌
        music_played = (music * play_time)[:play_time]
        
        # 네오가 들은 게 맞는지 체크
        if m in music_played:
            if play_time > answer[1]:
                answer = (title, play_time)
    
    return answer[0]