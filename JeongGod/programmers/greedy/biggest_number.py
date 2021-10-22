def solution(number, k):
    # 내림차순으로 진행된다면 무조건 큰 수가 나옴.
    """
    1. 첫자리를 일단 tmp에 넣음.
    2. tmp의 숫자와 현재 넣을 숫자를 비교
        1. tmp[i] >= 현재 넣을 숫자
            => 진행
        2. tmp[i] < 현재 넣을 숫자
            => tmp[i]제거 (k가 0이거나 1번의 조건에 만족될 때 까지)
    3. tmp에 현재 넣을 숫자 추가
    """
    tmp = list(number[0])
    max_len = len(number)-k
    for num in number[1:]:
        for i in range(len(tmp)-1, -1, -1):
            if tmp[i] >= num or k == 0:
                break
            tmp.pop()
            k -= 1
        tmp += num

    return "".join(tmp[:max_len])
