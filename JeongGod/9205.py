'''
처음 20병
50m당 한 병씩 줄어듬 50m일 때, 맥주가 없으면 fail
편의점을 들리면 20병 리필

1. 페스티벌장까지의 거리를 계산
    (맥주의 수) * 50보다 작거나 같다면 => Happy
    만약 크다면,
        현재 내가 갈 수 있는 편의점을 들린다.
        맥주를 다시 채우고, 1번을 반복한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    start = list(map(int, input().split()))
    faci = [list(map(int, input().split())) for _ in range(n)]
    dest = list(map(int, input().split()))

    def check(dist, beer):
        if dist <= (beer)*50:
            return True
        return False

    # 좌표상의 거리를 구해보자.
    dq = deque([(20, start)])
    flag = False
    while dq:
        beer, cur = dq.popleft()
        dist = abs(cur[0] - dest[0]) + abs(cur[1] - dest[1])
        if check(dist, beer):
            flag = True
            break
        # 편의점중 가능한 거리인 편의점을 다 들린다.
        for idx, elem in enumerate(faci):
            dist = abs(cur[0] - elem[0]) + abs(cur[1] - elem[1])
            if check(dist, beer) and (elem[0] != -40000 and elem[1] != -40000):
                beer = 20
                next = [elem[0], elem[1]]
                # 방문처리
                faci[idx][0] = -40000
                faci[idx][1] = -40000
                dq.append((beer, next))
    if flag:
        print("happy")
    else:
        print("sad")
