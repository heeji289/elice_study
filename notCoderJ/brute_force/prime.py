'''
  풀이 요약
    에라토스테네스의 체를 이용해 주어진 숫자의 최대 숫자까지의 소수를 구합니다.
    주어진 숫자들의 모든 조합을 구하며 소수인 숫자들을 answer에 추가합니다.
    이후 answer의 길이를 반환합니다.
'''

def solution(numbers):
    answer = set()
    numbers = ''.join(sorted(numbers, reverse=True))
    nlen = len(numbers)
    
    # 에.토.체
    prime = [True for _ in range(int(numbers) + 1)]
    prime[0], prime[1] = False, False
    for n in range(2, int(numbers) + 1):
        if prime[n]:
            for i in range(n * 2, int(numbers) + 1, n):
                prime[i] = False
                
    def comb(cnt, nums):
        nonlocal answer
        if cnt == 0:
            answer |= set(filter(lambda x: prime[x], [int(''.join(nums))]))
        
        for i, v in enumerate(numbers):
            if visited[i]:
                continue
            visited[i] = True
            comb(cnt - 1, nums + [v])
            visited[i] = False
    
    for i in range(1, nlen + 1):
        visited = [False] * nlen
        comb(i, [])

    return len(answer)