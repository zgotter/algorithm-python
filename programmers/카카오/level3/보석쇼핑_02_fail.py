# 일부 테스트 케이스 실패
#  - 시간초과: 2, 3, 8~15 나머지 모든 효율성 테스트

from collections import defaultdict
from itertools import product

def solution(gems):
    gem_dict = defaultdict(list)
    for i, gem in enumerate(gems):
        gem_dict[gem].append(i+1)
    idx_list = [lst for lst in gem_dict.values()]
    unique_gems = [gem for gem in gem_dict]

    range_len = 100000
    answer = []
    for lst in product(*idx_list):
        min_val, max_val = min(lst), max(lst)
        if max_val - min_val + 1 < range_len:
            range_len = max_val - min_val + 1
            answer = [min_val, max_val]
    
    return answer