# 효율성 테스트 실패

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        check = [s for s in scoville if s >= K]
        if len(check) == len(scoville):
            break
        
        if len(scoville) == 1:
            answer = -1
            break
            
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        new_food = food1 + (food2 * 2)
        heapq.heappush(scoville, new_food)
        
        answer += 1
    return answer