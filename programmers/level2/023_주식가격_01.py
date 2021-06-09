# 대부분의 테스트 케이스 실패 (시간 줄여야 됨)

def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    for i in range(n):
        p = prices[i]
        for j in range(i+1, n):
            if p <= prices[j]:
                answer[i] += 1
    return answer