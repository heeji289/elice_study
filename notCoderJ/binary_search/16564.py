'''
    풀이 요약
        주어진 N개의 수를 반씩 분할하여 경우의 수를 줄여나가는 이분 탐색의 원리를 활용했습니다.
        이분 탐색처럼 반씩 분할하진 않지만 총 렙업 가능한 값(k)에서 인접한 렙업까지 필요한 값 * 렙업힐 케릭터 수를 계속 차감해주면서 k를 줄여 나갔습니다.
        
        인접한 두 레벨의 차이에 현재 인덱스 + 1(해당 레벨까지 렙업할 캐릭터 수를 의미)을 곱하여 이 값이 k보다 작으면 해당 값을 k에서 빼고 현재 최소 레벨(answer)을 둘 중 큰 레벨로 변경합니다. 만약 k보다 크거나 같다면 남은 k를 현재 렙업할 캐릭터 수로 나눈 몫을 현재 최소 렙에 추가하여 출력합니다.
'''
import sys
input = lambda: sys.stdin.readline().rstrip()


def goalLevel(n, k, levels):
    answer = levels[0]

    for i in range(n - 1):
        upReq = (levels[i + 1] - levels[i]) * (i + 1)
        if k > upReq:
            k -= upReq
            answer = levels[i + 1]
        else:
            answer += k // (i + 1)
            return answer


if __name__ == "__main__":
    n, k = map(int, input().split())
    levels = sorted([int(input()) for _ in range(n)])
    print(goalLevel(n, k, levels))