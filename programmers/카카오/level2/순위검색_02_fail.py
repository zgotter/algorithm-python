# 효율성 테스트 실패
# - 점수 이진탐색 미적용

from itertools import combinations
from collections import defaultdict

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
            match_scores = [score for score in scores if score >= query_score]
            answer.append(len(match_scores))
        else:
            answer.append(0)
        
    return answer