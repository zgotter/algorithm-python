# 실패 (시간 초과)

from itertools import permutations

def is_prime(n):
    A, p = [0 for _ in range(n+1)], []
    for i in range(2, n):
        if A[i] == 0:
            p.append(i)
        else:
            continue
        for j in range(i**2, n, i):
            A[j] = i
    
    if n-1 in p:
        return True
    else:
        return False

def solution(numbers):
    answer = 0
    num_lst = []
    for i in range(len(numbers)):
        for comb in permutations(list(numbers), i+1):
            val = int(''.join(comb))
            if val not in num_lst:
                num_lst.append(val)

    for num in num_lst:
        if is_prime(num+1):
            answer += 1
    return answer