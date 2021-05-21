def gcd(a, b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return i

def solution(n, m):
    answer = [gcd(n, m), int((n*m)/gcd(n, m))]
    return answer

print(solution(3,12))
print(solution(2,5))