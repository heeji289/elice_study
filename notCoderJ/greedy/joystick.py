'''
    풀이요약
        1. A가 아닌 문자를 찾으며 커서를 이동시켜갑니다.
        2. 이전 커서 위치에서 마지막 'A'가 아닌 문자까지 이동 거리와 반대 방향으로 현재 위치에 도달했을 때 이동거리를 비교합니다.
            2-1. 반대 방향이 더 짧은 경우 방향을 회전하고 현재 위치까지 오는 거리를 더해줍니다.
            2-2. 반대의 경우 현재 위치 - 이전 위치를 계속 더해줍니다.
        3. 문자 변환 시 최소 이동 값을 더해줍니다.
'''
def solution(name):
    answer, cursor, back = 0, 0, False
    total = len(name)
    last = total - 2 if name[::-1].find('A') == 0 else total - 1
    for i, w in enumerate(name):
        if w == 'A':
            continue
        if i - cursor > total - last + cursor:
            back = True
            answer += total - i + cursor
        answer += 0 if back else i - cursor
        answer += min(ord(w) - ord('A'), ord('Z') - ord(w) + 1)
        cursor = i
    
    return answer