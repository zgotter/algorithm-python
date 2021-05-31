# 일부 테스트 케이스 실패

def solution(s):
    if s[0] == ')': return False
    c = 0
    for a in s: c += 1 if a == '(' else -1
    return not c