'''
  풀이요약
    1. 최초 버스 시간(09:00)을 분으로 변경하고 모든 버스 시간을 구합니다.
    2. 대기열 테이블 시간들을 모두 분으로 변경한 후 오름차 정렬합니다.
    3. 버스 시간을 하나씩 순회하며 해당 버스에 대기열 테이블에서 태울 수 있는 수만큼 태웁니다.
    4. 모든 버스에 태우고 난 후 마지막 버스에 탑승 인원을 확인합니다.
      4-1. 인원이 꽉찼으면 가장 늦게 탄 사람의 시간 - 1분을 반환합니다.
      4-2. 인원이 넉넉하면 마지막 버스 시간을 반환합니다.
'''

def solution(n, t, m, timetable):
    conv = lambda x: int(x[0]) * 60 + int(x[1])
    minutes = lambda x: conv(x.split(':'))
    rconv = lambda x: f'{x // 60:02}:{x % 60:02}'
    
    buses = [minutes("09:00") + i * t for i in range(n)]
    timetable = sorted([minutes(t) for t in timetable], reverse=True)

    for bus in buses:
        st = []
        while len(st) < m and timetable:
            if bus >= timetable[-1]:
                st.append(timetable.pop())
            else:
                break
    return rconv(buses[-1]) if len(st) < m else rconv(st[-1] - 1)