# 2018 카카오 블라인드 3차 파일명 정렬

"""
참고한 풀이 ^^ : https://m.post.naver.com/viewer/postView.naver?volumeNo=27023886&memberNo=33264526

파일명에 포함된 숫자를 기준으로 정렬하고 싶다
head - number(1~5) - tail

분리를 해서 정리해둬야할 것 같다..

1. head를 기준으로 정렬 / 대소문자 구분 안함 => 그럼 하나하나 사전순으로 봐야되나..
2. number순으로 정렬
3. 그 다음부터는 주어진 순서를 유지
"""

import re

def solution(files):
    # r''은 백슬래시 안써도되서 편하다
    # 숫자에 해당하는 애들을 정규표현식으로 찾고 얘를 중심으로 분리한다
    files = [re.split(r"([0-9]+)", file) for file in files]
    
    # head부분을 소문자로 변환해서 비교 => number부분 비교
    sorted_files = sorted(files, key=lambda x: (x[0].lower(), int(x[1])))
    
    # 다시 원래모양으로 합친다
    return [''.join(s) for s in sorted_files]