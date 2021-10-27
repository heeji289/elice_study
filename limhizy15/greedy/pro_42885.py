# 최소한 필요한 구명보트 개수..

"""
50 50 70 80 => 80, 70, 50 + 50
50 70 80 => 80, 70, 50
"""

def solution(people, limit):
    answer = 0
    
    people.sort() # 오름차순 정렬
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        answer += 1
        
        # 지금 기준 제일 작은 + 큰 애를 같이 태울 수 있으면 태운다
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1 # 무게 제한이 최댓값보다 크게 주어지니까 무조건 1개엔 태울 수 있다
    
    return answer