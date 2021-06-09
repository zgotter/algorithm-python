# 대부분의 테스트 케이스 실패 (시간 줄여야 됨)

from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    for i in range(n):
        p = prices[i]
        queue = deque(prices[i+1:])
        while queue:
            v = queue.popleft()
            if p <= v:
                answer[i] += 1
    return answer