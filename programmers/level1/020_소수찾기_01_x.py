# 정확도 테스트 일부 실패
# 효율성 테스트 실패

def is_prime(n):
    res = True
    for i in range(2, n):
        if n % i == 0:
            res = False
            break
    return res

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_prime(i): answer += 1
    return answer