"""
1. 캐시크기만큼 배열을 생성한다. 아니면 큐
2. miss일 경우 배열에 넣는다. 만약 꽉 차있다면 맨 앞을 방출하고 넣는다
3. hit일 경우 해당 요소를 배열에서 빼고 맨 뒤로 옮긴다 (최신.. 갱신 느낌으로)

예외
- 캐시 크기가 0일 때..
- 도시는 대소문자 구분이 없으므로.. 똑같이 소문자로 만들어서 처리할 것
"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0: 
        return len(cities) * 5
    
    cache = deque()
    
    for city in cities:
        # print("cache:", cache, "city", city.lower(), "answer:", answer)
        # cache miss인 경우!
        if city.lower() not in cache:
            cache.append(city.lower())
            answer += 5
            if len(cache) > cacheSize:
                cache.popleft()
        else:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
            
    return answer