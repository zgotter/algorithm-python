# 성공

def solution(s):
    l = len(s)
    ll = len(s)//2
    if l % 2 == 1:
        return s[ll]
    else:
        return s[ll-1:ll+1]