# 대부분의 테스트 케이스 실패 (시간 줄여야 됨)

def solution(prices):
    answer = []
    for i in range(len(prices)):
        p = prices[i]
        lst = [l-p for l in prices[i+1:] if l-p >= 0]
        answer.append(len(lst))
    return answer