# 1개 테스트 케이스 실패 (시간 초과)

from itertools import combinations

def solution(clothes):
    dic = dict()
    for name, tp in clothes:
        if tp in dic.keys():
            dic[tp].append(name)
        else:
            dic[tp] = [name]
    lst = [len(dic[key]) for key in dic.keys()]
    ans = 0
    for i in range(1, len(lst)+1):
        for values in combinations(lst, i):
            v = 1
            for value in values:
                v *= value
            ans += v
    return ans