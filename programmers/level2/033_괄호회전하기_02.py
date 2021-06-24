# 1개 테스트 케이스(14) 실패
#  - chk() 함수 값 0보다 큰 경우 처리 후 12, 13 성공
#  - "([{)}]" 처리 필요

def chk(s):
    dic = {'()': 0, '{}': 0, '[]': 0}
    for ss in s:
        for key in dic.keys():
            if ss in key:
                if dic[key] < 0:
                    return False
                if ss == key[0]:
                    dic[key] += 1
                else:
                    dic[key] -= 1
    for key in dic.keys():
        if dic[key] != 0:
            return False
    return True

def solution(s):
    n = len(s)
    lst = [s[i:n] + (s[0:i] if i != 0 else '') for i in range(n)]
    return sum([chk(l) for l in lst])
