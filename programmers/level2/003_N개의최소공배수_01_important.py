# 성공

def gcd(a,b):
    return gcd(b, a%b) if a%b != 0 else b

def lcm(a,b):
    return int(a*b/gcd(a,b))

def solution(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = lcm(ans, arr[i])
    return ans