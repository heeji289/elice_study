people = [70, 50, 80, 50]
limit = 100
from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while people:
        try:
            light = people[0]
            heavy = people[-1]
            if light + heavy <= limit:
                answer += 1
                people.popleft()
                people.pop()
            else:
                answer += 1
                people.pop()
        except:
            if len(people) == 1:
                answer += 1
                people.pop()
        
    return answer


print(solution(people, limit))
