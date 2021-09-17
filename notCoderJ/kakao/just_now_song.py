'''
  풀이 요약
    1. 주어진 play 리스트를 순회하며 각 재생 시간을 분으로 변환하고 해당 시간만큼 가사를 늘립니다.
    2. 찾고자하는 가사(m)가 1번에서 play한 길이만큼의 가사에 포함되어 있는지 정규식을 통해 확인합니다.
      (이때 가사(m) 바로 뒤에 '#'이 아닌 것이 오거나 아무것도 없는 경우만을 골라냅니다)
    3. 만약 2번에서 골라진 경우 answer에 (play 시간, 인덱스, 음악 이름)을 추가합니다.
    4. answer가 빈 경우 '(None)'을 반환하고
      아닌 경우 answer를 play시간은 내림차로, 인덱스는 오름차로 정렬 후 가장 앞에 있는 음악 이름을 반환합니다.
'''

import re

def solution(m, musicinfos):
    answer = []
    to_min = lambda x: int(x[:2]) * 60 + int(x[3:]) # 분 계산
    minutes = lambda s, e: to_min(e) - to_min(s)

    for i, (s, e, n, l) in enumerate([x.split(',') for x in musicinfos]):
        mins = minutes(s, e)
        plen = len(l.replace('#', ''))
        lyrics = l * (mins // plen)
        remain = re.match('([A-G]#?){{{}}}'.format(mins % plen), l)
        lyrics += remain.group() if remain else ''

        if re.match(f'.*{m}(?!#)', lyrics):
            answer.append((mins, i, n))
            
    return sorted(answer, key=lambda x: (-x[0], x[1]))[0][2] if answer else '(None)'