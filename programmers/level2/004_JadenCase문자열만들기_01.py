# 일부 테스트케이스 실패

def solution(s):
    return ' '.join([l[0].upper() + l[1:].lower() for l in s.split(' ')])