# 처음 dict로 푼 것
def solution(cacheSize, cities):
    """
    LRU => 최근 사용했던 친구는 가장 나중에 빠진다.
    """
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = dict()

    for city in map(str.lower, cities):
        # Miss
        if city not in cache:
            # 제일 늦게 쓰인 놈을 찾는다.
            if len(cache) == cacheSize:
                tmp = max(cache.items(), key=lambda x: x[1])
                cache.pop(tmp[0])
                cache[city] = 0
            else:
                cache[city] = 0
            answer += 5
        # Hit
        else:
            cache[city] = 0
            answer += 1

        cache = dict(map(lambda x: (x[0], x[1]+1), cache.items()))
    return answer


# Queue사용


def solution(cacheSize, cities):
    from collections import deque
    """
    LRU => 최근 사용했던 친구는 가장 나중에 빠진다.
    => queue잖아..
    """
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = deque([])

    for city in map(str.lower, cities):
        # Miss
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
        # Hit
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer
