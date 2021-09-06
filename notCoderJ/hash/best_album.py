'''
  풀이요약
    1. 각 장르별로 전체 플레이 수와 (각 음악의 플레이 수, 고유번호의 음수 값)를 리스트 형태로 저장합니다.
    2. 장르를 전체 플레이 수 기준으로 내림차 정렬한 후 각 장르에서 음악 리스트들을 다시 내림차 정렬합니다.
    3. 장르별로 우선순위가 높은 2개의 음악을 선택해 answer에 저장해줍니다.
'''
from collections import defaultdict


def solution(genres, plays):
    answer = []
    play_cnt = defaultdict(list)
    for i, genre in enumerate(genres):
        if not play_cnt[genre]:
            play_cnt[genre].append(plays[i])
        else:
            play_cnt[genre][0] += plays[i]
        play_cnt[genre].append((plays[i], -i))

    for pl in sorted(play_cnt.values(), reverse=True):
        answer += list(map(lambda x: -x[1], sorted(pl[1:], reverse=True)))[:2]

    return answer
