# 성공

def get_notation(n, base):
    if n == 0: return '0'
    res = []
    while n > 0:
        n, r = divmod(n, base)
        res.append(str(r))
    trans = {str(i+10): chr(i+65) for i in range(6)}
    res = [trans[r] if r in list(trans.keys()) else r for r in res]
    return ''.join(reversed(res))

def solution(n, t, m, p):
    lst = list(''.join([get_notation(i, n) for i in range(t*m)]))
    res = [lst[i] for i in range(p-1, t*m, m)]
    return ''.join(res)