# 일부 테스트 케이스 실패
#  - 실패: 6, 7
#  - 시간초과: 11, 14, 나머지 모든 효율성 테스트

from collections import Counter

def solution(gems):
    answer = []
    unique = set(gems)
    cnt = len(unique)
    while True:
        if cnt == len(gems):
            answer = [1, cnt]
            break
        idx = -1
        for i in range(len(gems)-cnt):
            sub_gems = gems[i:i+cnt]
            if unique == set(sub_gems):
                idx = i
                break
        if idx != -1:
            answer = [i+1, i+cnt]
            break
        else:
            cnt += 1
    return answer