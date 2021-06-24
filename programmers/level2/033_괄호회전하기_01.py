# 3개 테스트 케이스(12, 13, 14) 실패

def chk(s):
    dic = {'()': 0, '{}': 0, '[]': 0}
    res = True
    for ss in s:
        for key in dic.keys():
            if ss in key:
                if dic[key] < 0:
                    return False
                if ss == key[0]:
                    dic[key] += 1
                else:
                    dic[key] -= 1
    return res

def solution(s):
    n = len(s)
    lst = [s[i:n] + (s[0:i] if i != 0 else '') for i in range(n)]
    return sum([chk(l) for l in lst])