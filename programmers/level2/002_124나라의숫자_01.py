# 01

def solution(n):
    answer = ''
    v = '412'

    while n:
        n, na = divmod(n,3)
        answer = v[na] + answer
        if not na:
            n -= 1

    return answer

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))