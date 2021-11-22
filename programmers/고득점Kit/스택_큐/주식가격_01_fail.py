# 효율성 테스트 5개 모두 실패

def solution(prices):
    answer = []
    for i in range(len(prices)):
        p = prices[i]
        after = prices[i+1:]
        t = 0
        if len(after) > 0:
            for a in after:
                t += 1
                if p > a:
                    break
        answer.append(t)
    return answer