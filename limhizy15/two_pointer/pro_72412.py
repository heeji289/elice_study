# 2021 kakao 순위 검색

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

# info - 4가지 정보 + 점수, query - 문의조건
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    
    # 정보 가공
    for i in info:
        temp = i.split(' ')
        four_infos = temp[:-1] # 4가지 정보
        score = int(temp[-1]) # 점수
        
        # 4가지 정보로 가능한 모든 조합을 만들어 딕셔너리의 키값으로 활용
        for k in range(5):
            for comb in combinations(four_infos, k):
                info_dict[''.join(comb)].append(score)
    
    # 이진 탐색을 위한 정렬
    for v in info_dict.values():
        v.sort()
    
    # 쿼리 가공
    for q in query:
        num = 0
        
        temp = q.split(' ')
        q_infos = temp[:-1]
        q_score = int(temp[-1])
        
        q_string = ''.join(q_infos)
        
        # and와 - 제거 
        q_string = q_string.replace('and', '')
        q_string = q_string.replace('-', '')
        
        # 그냥 탐색할 때 시간초과
        # 이진탐색 참고 - https://esoongan.tistory.com/119
        if q_string in info_dict:
            score_list = info_dict[q_string]
            # target 점수의 index를 찾은 후 전체 길이에서 index만큼 빼줌
            index = bisect_left(score_list, q_score)
            answer.append(len(score_list) - index)
        else:
            answer.append(0)
    
    return answer