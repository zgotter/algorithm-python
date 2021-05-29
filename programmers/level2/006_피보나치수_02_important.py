# 성공
# 동적계획법(DP) 활용

def fibo(n):
    lst = [0 for _ in range(n+1)]
    lst[1] = 1
    for i in range(2, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n]

def solution(n):
    return fibo(n) % 1234567