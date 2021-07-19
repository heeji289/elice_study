# 도영이가 만든 맛있는 음식

"""
[문제]
n개의 음식재료와 각 각의 신맛, 쓴맛 값이 주어진다.
신맛은 곱연산 쓴맛은 합연산으로 음식의 신맛, 쓴맛이 결정된다.
1개 이상의 재료를 선택했을 때 신맛과 쓴맛의 차이가 가장 작은 요리를 만들어라.

[풀이]
1) 1개씩부터 n개까지 조합을 모두구한다.
해당 요리의 신맛, 쓴맛을 구한다. 이 차이의 최솟값을 갱신한다.
2) 재귀로 해당 재료를 선택한다/안한다로.. 퇴사문제 풀때처럼 설계..
cnt로 1부터 n까지 탐색하면서 해당 재료를 선택함/선택안함
cnt가 n이되면 모든 재료 탐색이 완료되었으므로 종료 (최솟값 갱신)
"""

import sys

answer = 1e9  # 나올 수 있는 |신맛-쓴맛|의 최대

n = int(sys.stdin.readline())
ingredient = []
# flag = True

# 재료의 신맛, 쓴맛 저장
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    ingredient.append(tmp)

# print(ingredient)


def solve(cnt, s, b):
    global answer
    # 재료 끝까지 탐색 완료
    if cnt == n:
        # 초기호출 (0, 1, 0) => 얘도 계산이 되서 예외처리..
        if s == 1 and b == 0:
            return

        # print("s, b:", s, b)
        answer = min(answer, abs(s - b))
        return

    # 재료를 선택한 후 다음재료로 이동
    solve(cnt+1, s * ingredient[cnt][0], b + ingredient[cnt][1])
    # 재료 선택 안하고 다음재료로 이동
    solve(cnt+1, s, b)


# 신맛은 곱연산이므로 1로 초기화
solve(0, 1, 0)
print(answer)
