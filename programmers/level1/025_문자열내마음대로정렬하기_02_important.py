# 다른사람풀이
# lambda 사용
# 성공

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])