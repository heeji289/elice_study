# 퇴사

'''
[문제]
- 상담에 걸리는 기간과 해당 상담을 마치면 벌 수 있는 돈이 주어진다.
- N+1일에는 퇴사를 할 것이다. 이전까지 최대한 상담을 해서 벌 수 있는 최대수익은?

[풀이]
- 퇴사 전 어떤 날을 k일이라고 할 때
-> 오늘 예약에 잡혀있는 상담을 한다 혹은 하지 않는다 두 경우 중 하나를 고를 수 있다.
-> 상담을 하는 경우엔 해당 상담에 걸리는 기간에 들어오는 예약은 무시 -> 상담이 끝난 다음날로 이동
-> 상담을 하지 않는 경우엔 다음날로 이동

- k일이 N+1일이 되면 퇴사날이므로 지금까지 번 돈의 최댓값을 갱신
- k일이 N+1일보다 크다면 이전에 진행한 상담이 N일내에 끝낼 수 없었던 것이었으므로 체크하지 않아도 된다.
'''

import sys

answer = 0

n = int(sys.stdin.readline())
table = [[0] * 2 for _ in range(n+1)]  # 상담 테이블

for i in range(0, n):
    t, p = map(int, sys.stdin.readline().split())
    table[i][0] = t
    table[i][1] = p


def solve(day, money):
    global answer
    # 만약 퇴사날보다 큰 day가 들어온다면
    # 앞에서의 상담을 못하는 것
    if day > n:
        return

    # 퇴사날
    if day == n:
        answer = max(answer, money)  # 최댓값 갱신
        return

    # 상담 함 : 상담기간만큼 점프해서 해당날짜로, 돈 추가
    solve(day + table[day][0], money + table[day][1])
    # 상담 안함 : 그냥 다음날로 이동, 돈도 그대로
    solve(day+1, money)


# 1일부터 시작 (인덱스는 0)
solve(0, 0)
print(answer)
