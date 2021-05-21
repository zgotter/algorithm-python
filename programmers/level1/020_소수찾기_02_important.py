# 소수(prime number) 찾을 때 '에라토스테네스의 체' 활용
# - 성공

def era_prime(n):
    A, p = [0 for _ in range(n+1)], []
    for i in range(2, n):
        if A[i] == 0: p.append(i)
        else:
            continue
        for j in range(i**2, n, i):
            A[j] = 1
    return p

def solution(n):
    p_lst = era_prime(n+1)
    return len(p_lst)

print(solution(10))
print(solution(5))
