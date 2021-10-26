def solution(N, number):
    """
    괄호를 해결해야 한다.
    dp[1] = {N}
    dp[2] = {N*N, N+N, N-N, N//N, NN}
    dp[n] = dp[1] + dp[n-1], dp[2] + dp[n-2], dp[3] + dp[n-3] ...
    """
    def calc(n1, n2):
        tmp = set()
        for i in n2:
            for j in n1:
                tmp |= {i+j, i*j, abs(i-j)}
                if j != 0:
                    tmp |= {i // j}
                if i != 0:
                    tmp |= {j // i}
        return tmp - set(n1) - set(n2)

    dp = [set() for _ in range(10)]

    for i in range(1, 9):
        for j in range(1, i//2+1):
            dp[i] |= calc(dp[j], dp[i-j])
        dp[i].add(int(str(N)*i))
        if number in dp[i]:
            return i

    return -1
