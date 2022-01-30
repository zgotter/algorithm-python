# 정확성 테스트 성공, 효율성 테스트 실패

def solution(stones, k):
    answer = 0
    n = len(stones)
    while True:
        check = True
        for i in range(n-k+1):
            if sum(stones[i:i+k]) == 0:
                check = False
                break
        if not check:
            break
        answer += 1
        stones = [stone-1 if stone > 0 else 0 for stone in stones]        
    return answer