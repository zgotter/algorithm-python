# 테스트 케이스 대부분 실패

def solution(clothes):
    dic = dict()
    for name, tp in clothes:
        if tp in dic.keys():
            dic[tp].append(name)
        else:
            dic[tp] = [name]
    lst = [len(dic[key]) for key in dic.keys()]
    ans = 0
    if len(lst) == 1:
        ans = lst[0]
    else:
        ans += sum(lst)
        v = 1
        for a in lst:
            v *= a
        ans += v
    return ans