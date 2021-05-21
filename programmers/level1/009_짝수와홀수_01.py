from math import gcd

def solution(n, m):
    answer = [gcd(n, m), int((n*m)/gcd(n, m))]
    return answer

print(solution(3,12))
print(solution(2,5))