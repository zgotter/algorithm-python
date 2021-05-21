# 성공

def solution(s):
    p, y = 0, 0
    for x in s:
        if x.lower() == 'p':
            p += 1
        if x.lower() == 'y':
            y += 1
    if not p and not y:
        return True
    else:
        return p == y