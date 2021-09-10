def solution(numbers):

    # 모두 4자리로 만들어준다.    
    result = []
    for num in numbers:
        tmp = str(num)
        tmp += tmp*3
        result.append((tmp[:4], str(num)))
    
    # 4자리수로 sort한다. 만약 4자리수가 같다면, 기존에 있던 수로 비교를 한다.
    result = sorted(result, key=lambda x : (int(x[0]), int(x[1])), reverse=True )

    # 예외처리
    if result[0][1] == '0':
        return '0'
    
    answer = ''.join([x[1] for x in result])

    return answer
