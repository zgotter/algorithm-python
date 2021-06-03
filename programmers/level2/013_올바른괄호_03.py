# 성공

def solution(s):
    if s[0] == ')': return False
    c = 0
    for a in s:
        c += 1 if a == '(' else -1
        if c < 0: return False
    return not c