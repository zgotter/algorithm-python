# 성공

from collections import defaultdict

def solution(clothes):
    answer = 1
    dict_data = defaultdict(list)
    for key, val in clothes:
        dict_data[val].append(key)
    for key in dict_data.keys():
        answer *= len(dict_data[key])+1
    answer -= 1    
    return answer