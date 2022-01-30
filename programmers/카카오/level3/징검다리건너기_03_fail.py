# 정확성 테스트 성공, 효율성 테스트 실패
# 이분 탐색 기법 적용했지만, 효율성 테스트에서 시간 초과 발생

def solution(stones, k):
    start, end = 0, max(stones)
    while start < end:
        mid = (start + end) // 2
        temp_stones = [stone - mid for stone in stones]
        count = 0
        for temp_stone in temp_stones:
            if count == k:
                break
            if temp_stone <= 0:
                count += 1
            else:
                count = 0
        if count < k:
            start += 1
        else:
            end -= 1
    return start