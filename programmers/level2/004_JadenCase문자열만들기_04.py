# 성공

def solution(s):
    res = []
    for a in s.split(' '):
        w = []
        for i, v in enumerate(a):
            w.append(v if v.isdigit() else (v.upper() if i == 0 else v.lower()))
        res.append(''.join(w))
    return ' '.join(res)