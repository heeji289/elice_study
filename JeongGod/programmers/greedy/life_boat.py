def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    answer = 0

    while left < right:
        total = people[left] + people[right]
        if total <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1

    if left == right:
        answer += 1
    return answer
