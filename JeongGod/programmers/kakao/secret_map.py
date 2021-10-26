def solution(n, arr1, arr2):
    answer = []
    result = [0] * n
    for idx, val in enumerate(arr1):
        result[idx] = val
    for idx, val in enumerate(arr2):
        result[idx] |= val

    for idx, val in enumerate(result):
        tmp = ""
        for i in f"{bin(val)[2:]:0>{n}}":
            if i == "1":
                tmp += "#"
            elif i == "0":
                tmp += " "
        answer.append(tmp)
    return answer
