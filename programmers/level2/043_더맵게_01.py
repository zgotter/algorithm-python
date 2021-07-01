# 정확성 테스트 2개(2, 3) 실패
# 효율성 테스트 5개(1,2,3,4,5) 실패 (시간 초과)

def solution(scoville, K):
    res = 0
    while True:
        if min(scoville) >= K:
            break
        if len(scoville) == 1:
            res = -1
            break
        a = scoville.pop(0)
        b = scoville.pop(0)
        scoville.append(a + b*2)
        scoville.sort()
        res += 1
    return res