# 성공

def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        t = 0
        for j in range(i+1, n):
            t += 1
            if prices[i] > prices[j]:
                break
        answer.append(t)
    return answer