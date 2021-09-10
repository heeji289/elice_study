'''
  풀이요약
    bit 연산을 이용하기 위해 bit 테이블을 만들어서 이용했습니다.
    1. 가능한 선택지에 대해 종류별로 1bit씩 할당해서 아래와 같이 자리값을 지정합니다.
      언어는 최상위 3bit
      직종은 다음 상위 2bit
      경력은 그다음 상위 2bit
      음식은 최하위 2bit
    2. 주어진 info의 각 항목들을 해당 테이블을 이용해 값으로 치환해서 모두 더한 후
      그 값을 ap_cnt의 인덱스로 하여 코딩 테스트 점수를 추가합니다.
    3. 2에서 채워진 ap_cnt의 빈 값들을 모두 제거하고, (인덱스, 점수의 sorting 값) 형태로 변환합니다.
    4. 주어진 query를 파싱해서 2번과 같이 table을 이용해 위치 값으로 치환한 후
      해당 값과 ap_cnt의 인덱스를 and연산해서 query의 위치값과 동일한 경우
      이진 탐색을 이용해 현재 query의 점수보다 큰 점수의 갯수를 구해 해당 answer자리에 더해줍니다.
'''

from bisect import bisect_left

def solution(info, query):
    answer = [0] * len(query)
    # lang job career food
    #  000  00     00   00
    table = {
        'cpp': 256,
        'java': 128,
        'python': 64,
        'backend': 32,
        'frontend': 16,
        'junior': 8,
        'senior': 4,
        'chicken': 2,
        'pizza': 1,
    }
    
    ap_cnt = [[] for _ in range(512)]
    ap_info = map(lambda x: x.split(), info)
    
    for i, ap_if in enumerate(ap_info):
        ap_cnt[sum(map(lambda x: table[x], ap_if[:-1]))].append(int(ap_if[-1]))
    
    ap_cnt = [(i, sorted(v))  for i, v in enumerate(ap_cnt) if v]
    require = map(lambda x: x.replace('and', '').replace('-', '').split(), query)

    for i, req in enumerate(require):
        q = sum(map(lambda x: table[x], req[:-1]))
        for j, v in ap_cnt:
            if j & q == q:
                idx = bisect_left(v, int(req[-1]))
                answer[i] += len(v[idx:])
        
    return answer