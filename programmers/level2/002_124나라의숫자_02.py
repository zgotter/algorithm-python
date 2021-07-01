# 성공
# 복습
# 다른 사람 풀이 참고

def solution(n):
    answer = ''
    v = '412'
    while n:
        n, na = divmod(n, 3)
        answer = v[na] + answer
        if not na:
            n -= 1
    return answer