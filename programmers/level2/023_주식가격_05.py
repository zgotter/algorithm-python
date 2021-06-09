# 성공

def solution(prices):
    n = len(prices)
    answer = [0 for i in range(n)]
    for i in range(n):
        p = prices[i]
        for j in range(i+1, n):
            if p <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer