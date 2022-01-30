# 정확성 테스트 성공, 효율성 테스트 실패

def solution(stones, k):
    answer = 0
    n = len(stones)
    while True:
        #print(stones)
        if sum(stones) == 0:
            break
        idx = 0
        skip = 0
        while True:
            if idx == n:
                break
            if stones[idx] != 0:
                skip = 0
                stones[idx] -= 1
                idx += 1
            else:
                if skip < k-1:
                    skip += 1
                    idx += 1
                else:
                    break
        if idx == n:
            answer += 1
        else:
            break
    return answer