'''
  풀이 요약
    주어진 논문을 역순으로 정렬 후 위키피디아에 나온 h-index를 구하는 식에 따라
    (i in n) f(i) >= i를 적용하여 해당 식을 처음 만족하지 않을 때 이전 i(풀이에선 h)값을 반환해줍니다.
    만약 모두 위에 해당하지 않으면 모두 만족하는 것이므로 논문의 전체 길이를 반환합니다.
'''
def solution(citations):
    for h, v in enumerate(sorted(citations, reverse=True)):
        if v < h + 1:
            return h
    return len(citations)