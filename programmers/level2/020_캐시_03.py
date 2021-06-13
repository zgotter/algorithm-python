# 복습
# 성공

def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    for city in cities:
        if city not in cache: # miss
            answer += 5
            if len(cache) >= cacheSize:
                if len(cache) == 0: continue
                cache.pop(0)
            cache.append(city)
        else: # hit
            answer += 1
            cache.remove(city)
            cache.append(city)
    return answer