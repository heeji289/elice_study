"""
장르별 가장 많이 재생된 노래(고유 번호로 구분) 두개 씩 

노래 수록 기준
1. 장르에 속한 노래가 많이 재생된 순
2. 장르 내에서 많이 재생된 노래 순
3. 2가 같은 경우 고유 번호가 낮은 노래 먼저
"""
from collections import defaultdict

# 노래의 장르, 노래별 재생 횟수
# 앨범에 들어갈 노래의 고유 번호를 리턴
def solution(genres, plays):
    answer = []
    dic = defaultdict(dict)
    
    # dic 초기화
    for i in range(0, len(genres)):
        dic[genres[i]][i] = plays[i]
    
    # 재생횟수로 정렬
    most_played = sorted(dic.items(), key=lambda x: sum(x[1].values()), reverse=True)
    
    for item in most_played:
        # 장르 안에서 재생 횟수로 정렬
        music = item[1]
        sorted_music = sorted(music.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_music[0][1])
        if len(sorted_music) > 1:
            answer.append(sorted_music[0][0])
            answer.append(sorted_music[1][0])
        else:
            answer.append(sorted_music[0][0])
    return answer