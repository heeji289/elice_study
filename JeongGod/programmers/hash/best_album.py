def solution(genres, plays):
    _dict = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if _dict.get(genre) is None:
            _dict[genre] = [play, [(idx, play)]]
        else:
            _dict[genre][0] += play
            _dict[genre][1].append((idx, play))
    
    # _dict = {장르: [총 재생횟수, [(고유 번호,재생 횟수)]]}
    # 총 재생횟수로 정렬합니다.
    play_list = sorted(_dict.values(), key=lambda x: x[0], reverse=True)

    ans = []
    # 각각의 재생횟수로 정렬합니다. 만약 같다면 작은 고유번호순으로 정렬합니다.
    for li in play_list:
        top2 = sorted(li[1], key=lambda x: (x[1], -x[0]), reverse=True)
        if len(top2) >= 2:
            ans.append(top2[0][0])
            ans.append(top2[1][0])
        else:
            ans.append(top2[0][0])
    
    return ans
