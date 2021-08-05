'''
    풀이 요약
        1반 코치님 투 포인터 자료에 처음 등장하는 문제입니다.
        투 포인터의 개념을 설명하기 위한 문제같아요.
        
        먼저 각 인덱스까지의 합을 구한 리스트(sums)를 하나 생성합니다.
        i ~ j번째까지 수의 합을 SUM(i, j)라하면 SUM(i, j) = SUM(1, j) - SUM(1, i - 1)이 성립합니다.
        따라서, 주어진 (i, j) 값들을 순회하며 sums[j] - sums[i - 1] 값을 출력해줍니다.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, nums, parts):
    answer = []
    sums = [0]
    for num in nums:
        sums.append(sums[-1] + num)
    
    for i, j in parts:
        answer.append(sums[j] - sums[i - 1])
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    parts = (map(int, input().split()) for _ in range(m))
    print(*solution(n, m, nums, parts), sep='\n')