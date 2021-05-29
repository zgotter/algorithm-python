# 성공

def solution(s):
    res = []
    for a in s.split(' '):
        res.append(''.join([v if v.isdigit() else (v.upper() if i==0 else v.lower()) for i, v in enumerate(a)]))
    return ' '.join(res)