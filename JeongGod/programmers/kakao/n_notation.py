def solution(n, t, m, p):
    answer = ''
    """
    n : n진법
    t : t개의 숫자까지만 구한다. (종료 조건)
    m : m개의 인원이 돈다. (루프 돌 때)
    p : 순서 (루프의 시작 조건)
    """
    _dict = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

    def change(n, num):
        result = ""
        while num > 0:
            tmp = num % n
            if tmp >= 10:
                tmp = _dict.get(tmp)
            result += str(tmp)
            num //= n
        return result[::-1]

    total_n = "0"
    cnt = 1
    # tmp_n에 100만까지의 길이를 채워넣는다.
    while len(total_n) <= 1_000_000:
        total_n += change(n, cnt)
        cnt += 1
    # 튜브가 말해야 하는 숫자를 적어넣는다.
    for i in range(p-1, len(total_n), m):
        if len(answer) == t:
            break
        answer += total_n[i]
    return answer
