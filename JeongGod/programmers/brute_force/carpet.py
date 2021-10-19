def solution(brown, yellow):
    answer = []
    # yellow의 약수를 모두 구한다.
    yellow_m = []
    for i in range(1, yellow+1):
        if i * i > yellow:
            break
        if yellow % i == 0:
            yellow_m.append(i)

    # yellow의 약수를 하나씩 brown의 개수와 맞는지 비교한다.
    """
    m : 노란색의 세로 길이
    other_m : 노란색의 가로 길이
    """
    for m in yellow_m:
        other_m = yellow // m
        total = (m + 2) * 2 + other_m * 2
        if total == brown:
            return [other_m+2, m+2]
    return None
