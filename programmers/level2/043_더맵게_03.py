# 정확성 테스트 모두 성공
# 효율성 테스트 1개(5) 실패 (시간 초과)

import heapq

def solution(scoville, K):
    queue = []
    for s in scoville:
        heapq.heappush(queue, [s, s])
    res = 0
    while True:
        if len(queue) == 1 and queue[0][0] < K:
            res = -1
            break
        if queue[0][0] >= K:
            break
        a, _ = heapq.heappop(queue)
        b, _ = heapq.heappop(queue)
        v = a + (b*2)
        heapq.heappush(queue, [v, v])
        res += 1
    return res