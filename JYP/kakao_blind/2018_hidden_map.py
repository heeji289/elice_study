# 10진법 >> 2진법 변환(str로 내보내기)
def get_binary(num):
    temp = num
    rests = []

    if num == 0: # 예외 처리
        return 0

    while temp > 0:
        share, rest = divmod(temp, 2)
        rests.append(str(rest))
        temp = share

    return ''.join(rests[::-1])

    
def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        result = ""
        sum = str(int(get_binary(a1)) + int(get_binary(a2)))
        len_sum = len(str(sum))
        if n - len_sum != 0:
            sum = '0' * (n - len_sum) + sum

        for num in sum:
            result += '#' if int(num) > 0 else ' '
        answer.append(result)

    return answer
