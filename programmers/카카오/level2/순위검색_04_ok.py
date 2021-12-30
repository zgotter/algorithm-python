# 성공
# 이진탐색 라이브러리 bisect 사용

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info_list = info.split(" ")
        info_score = int(info_list[-1])
        info_list = info_list[:-1]
        for i in range(5):
            for comb in combinations(info_list, i):
                key = ''.join(comb)
                info_dict[key].append(info_score)
    
    for key in info_dict:
        info_dict[key].sort()
        
    for query in queries:
        query_list = query.split(" ")
        query_list = [q for q in query_list if q not in ["and", "-"]]
        query_score = int(query_list[-1])
        query_list = query_list[:-1]
        
        key = "".join(query_list)
        
        if key in info_dict:
            scores = info_dict[key]
            point = bisect_left(scores, query_score)
            answer.append(len(scores) - point)
        else:
            answer.append(0)
        
    return answer