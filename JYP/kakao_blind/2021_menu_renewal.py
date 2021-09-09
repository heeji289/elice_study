from collections import Counter
from itertools import combinations

def solution(orders, course):

    temp = [[]*i for i in range(len(course))]
    for order in orders:
        order = sorted(list(order))
        i = 0
        for num in course:
            temp[i] += list(map(''.join, combinations(order, num)))
            i += 1
            
    answer = []

    for combination in temp:
        count = Counter(combination)
        arr = [k for k, v in count.items() if max(count.values())==v and v > 1]
        answer += arr

    return sorted(answer)