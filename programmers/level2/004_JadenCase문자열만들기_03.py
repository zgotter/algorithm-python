# 성공

def solution(s):
    res = []
    for a in s.split(' '):
        w = []
        for i, v in enumerate(a):
            if v.isdigit(): w.append(v)
            elif i == 0: w.append(v.upper())
            else: w.append(v.lower())
        res.append(''.join(w))
    return ' '.join(res)