"""
clothes가 주어질 때 서로 다른 옷의 조합의 수 ? 
종류별로 딕셔너리를 만들어서 모은다
1. 하나씩 착용하는 것
2. 두 개를 골라 착용하는 것 (서로 다른 종류에서), 세 개 고르고.. ..
- 그럼 종류별 이름 개수들 곱하면 되지 않을까..? 곱해서 -1?
- 가지수 찾기 (개수 + 1) * (개수 + 1)..
"""
from collections import defaultdict

# clothes : [이름, 종류]
def solution(clothes):
    answer = 0
    dict_ = defaultdict(list)
    
    # clothes를 돌면서 딕셔너리에 값 넣기
    for item in clothes:
        dict_[item[1]].append(item[0])
    
    # 각 옷 종류에 대해 개수 찾기
    mul_ = 1
    
    for key, value in dict_.items():
        mul_ *= (len(value) + 1)
    
    answer = mul_ - 1
    return answer