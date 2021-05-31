# 일부 테스트 케이스 실패

def solution(s):
    if s[0] == ')': return False
    c = 0
    chk = False
    for a in s:
        if a == '(':
            if chk and c != 0: return False
            chk = False
            c += 1
        else:
            chk = True
            c -= 1
    return not c