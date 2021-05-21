# 성공

def solution(s):
    a = [i for i in s if i.lower() == i]
    A = [i for i in s if i.upper() == i]
    a.sort(reverse=True)
    A.sort(reverse=True)
    return ''.join(a) + ''.join(A)