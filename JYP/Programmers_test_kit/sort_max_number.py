from collections import defaultdict

def solution(numbers):

    if set(numbers) == {0}:
        return '0'
    
    keys = defaultdict(int)
    for num in numbers:
        first_digit = int(str(num)[0])

        if first_digit in keys:
            keys[first_digit].append(num)
        else:
            keys[first_digit] = [num]

    keys = sorted(dict.items(keys), reverse=True)

    answer = ""
    for key in keys:
        temp = sorted(key[1], key=lambda x: str(x)*3, reverse=True)
        for num in temp:
            answer += str(num)
            

    return answer