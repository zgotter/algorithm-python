# 성공
# 다른 사람 풀이 참고 (https://dev-note-97.tistory.com/70)
# 핵심 아이디어: 투 포인터 알고리즘

from collections import defaultdict

def solution(gems):
    answer = []
    range_len = len(gems)+1
    unique_gem_cnt = len(set(gems))
    start, end = 0, 0
    gem_dict = defaultdict(int)
    
    while end < len(gems):
        gem_dict[gems[end]] += 1
        end += 1
        if len(gem_dict) == unique_gem_cnt:
            while start < end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start += 1
                elif range_len > end - start:
                    range_len = end - start
                    answer = [start+1, end]
                    break
                else:
                    break
    return answer