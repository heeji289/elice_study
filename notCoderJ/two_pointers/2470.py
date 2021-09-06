'''
    풀이 요약
        허... INF값을 처음에 int(1e9)로 설정했다가 계속 실패해서 원인을 못찾고 한참 헤매고 있었는데
        다시 조건을 보니 용액 값이 -1,000,000,000 ~ 1,000,000,000 범위라서 값이 1e9만 들어올 경우 때문이었네요;;
        
        주어진 용액을 오름차 정렬한 후 양 끝단에 포인터를 두어 두 용액을 섞기 시작합니다.
        두 용액의 합에 따라 다음 중 하나를 수행합니다.
            1. 두 용액의 합이 양수: 우측 인덱스를 1 감소
            2. 두 용액의 합이 음수: 좌측 인덱스를 1 즐가
        위와 같이 하는 이유는 이미 정렬된 상태의 값들에서 양측의 합이 양수라는 것은 양의 값이 더 크다는 것이고
        좌측 인덱스를 증가시키면 양의 값이 더 증가하므로 양의 인덱스를 감소시켜 합의 차이를 줄여나가서 0으로 수렴하기 위함입니다. 
        음수인 경우 역시 위와 반대로 생각하면 됩니다.
        위 과정을 수행하며 현재 혼합물의 절대값이 기존 혼합물의 최소값보다 작으면 혼합물의 용액들로 기존 값을 갱신해줍니다.
'''
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

def solution(n, solutions):
    answer = [INF]
    s, e = 0, n - 1

    for _ in range(n - 1):
        mix = solutions[s] + solutions[e]
        if abs(mix) < answer[0]:
            answer = [abs(mix), solutions[s], solutions[e]]
            if mix == 0: break
        s, e = [(s + 1, e), (s, e - 1)][mix > 0]
        if s == e: break

    return answer[1:]


if __name__ == "__main__":
    n = int(input())
    solutions = sorted(list(map(int, input().split())))
    print(*solution(n, solutions))