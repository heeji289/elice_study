'''
  풀이요약
    리스트를 이용해 LRU 알고리즘으로 동작하는 캐시를 구현하여 풀이했습니다.
    각 도시들을 순회하며 캐시에 hit되는 경우 answer +1을 해주고 캐시에서 해당 도시를 꺼내 맨 끝으로 넣어줍니다.
    캐시에 없는 경우 answer +5를 하고, 캐시의 현재 크기에 따라 해당 도시를 캐시에 넣거나 가장 오래된 도시를 꺼낸 후 캐시에 넣어줍니다.
'''
def solution(cacheSize, cities):
    answer = 0
    if not cacheSize:
        return len(cities) * 5
    cities = [city.lower() for city in cities]
    lru = []
    
    for city in cities:
        if city not in lru:
            if len(lru) < cacheSize:
                lru.append(city)
            else:
                lru.pop(0)
                lru.append(city)
            answer += 5
        else:
            lru.append(lru.pop(lru.index(city)))
            answer += 1
    
    return answer