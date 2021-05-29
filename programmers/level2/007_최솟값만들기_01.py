# 성공

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    lst = [a*b for a, b in zip(A, B)]
    return sum(lst)