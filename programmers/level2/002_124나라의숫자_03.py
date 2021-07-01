# 성공
# 복습

def solution(n):
    answer = ''
    v = '412'
    while n:
        n, na = divmod(n, 3)
        answer = v[na] + answer
        if na == 0:
            n -= 1
    return answer