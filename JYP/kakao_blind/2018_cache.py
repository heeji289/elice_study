from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    cities_dict = dict()

    for city in cities:

        # 대소문자 구분 없애기 >> 소문자로 통일
        city = city.lower()
        
        # Cache Hit
        try:
            # 캐시 히트일 때 캐시에서 가장 최신 위치로 올려주고 시간 계산하기
            if cities_dict[city] == 1:
                idx = cache.index(city)
                cache.rotate(-idx) 
                cache.popleft() 
                cache.rotate(idx) # 원래 데이터 순서대로 정렬한 뒤
                cache.append(city) # 캐시의 최신 위치에 지금 읽은 값 추가
                answer += 1

        
        # Cache Miss
        except:
            # 캐시 사이즈가 0이면 계속 캐시 미스가 발생하므로 5초씩 추가
            if cacheSize == 0:
                answer += 5

            else:
                # 캐시가 꽉 찼다면 먼저 캐시에서 오래된 데이터를 제거하기
                if len(cache) >= cacheSize:
                    remove_city = cache.popleft()
                    del cities_dict[remove_city]
                
                # 캐시 및 참조 맵에 데이터 추가
                cache.append(city)
                cities_dict[city] = 1
                answer += 5

    return answer




'''
# TEST CASES

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# # return 50

# cacheSize = 5
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# # return 52

# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# # return 25

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
# return 16

# cacheSize = 5
# cities = ["Seoul", "Seoul", "Seoul"]
# # return 7

print(solution(cacheSize, cities))
'''
