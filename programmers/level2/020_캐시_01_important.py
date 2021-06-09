# 캐시 교체 알고리즘 LRU(Least Recently Used) 내용 검색하여 참고
# 성공

"""
LRU(Least Recently Used)
 - 캐시 교체 알고리즘
 - 사용자에게 빠르게 정보를 제공하기 위해 사용하는 캐시에서 새로운 데이터가 발생했을 때, 
   가장 오래전에 사용된 데이터를 제거하고 새로운 데이터를 삽입하는 알고리즘

LRU 구성
 1. 새로운 데이터가 들어온 경우 (miss)
  - 캐시에 넣어준다.
  - 캐시가 가득 차 있다면 가장 오래된 데이터를 제거하고 넣어준다.

 2. 캐시에 존재하는 데이터가 들어온 경우 (hit)
  - 캐시에서 해당 데이터를 제거한다.
  - 가장 최근 위치에 데이터를 넣어준다.
"""

def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    for city in cities:
        if city not in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if len(cache) == 0: continue
                cache.pop(0)
                cache.append(city)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
    return answer