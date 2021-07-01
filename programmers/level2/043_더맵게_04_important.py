# 성공
# 힙(Heap) 자료구조 활용

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    res = 0
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            res = -1
            break
        if scoville[0] >= K:
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b*2))
        res += 1
    return res