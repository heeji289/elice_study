'''
    희지님이 푸셨던 n과 m(1) 풀이입니다.
    제가 풀었던 방식보다 희지님이 푸셨던 방식이 훨씬 깔끔하고 좋은 것 같아서
    그 방식을 채용해서 다시 풀어봤습니다. 기록용 커밋입니다. ㅎㅎ
'''

import sys
input = lambda: sys.stdin.readline().rstrip()


def permutations(n, m, data, chk):
    if m == 0:
        print(*data)
        return
    
    for i in range(1, n + 1):
        if not chk[i]:
            chk[i] = True
            nums[-m] = i
            permutations(n, m - 1, data, chk)
            chk[i] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = [0] * m
    chk = [False for _ in range(n + 1)]
    permutations(n, m, nums, chk)