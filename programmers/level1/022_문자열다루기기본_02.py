# 길이 체크 조건을 고려하여 해결

def solution(s):
    return (s.isdigit() and len(s) in [4,6])