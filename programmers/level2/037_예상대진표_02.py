# 성공

def get_max_r(n):
    r = 0
    while n > 1:
        n = n // 2
        r += 1
    return r

def make_nxt_n(n):
    return (n if n % 2 ==0 else n+1) // 2

def solution(n,a,b):
    p = sorted([a, b])
    ans = 0
    for r in range(1, get_max_r(n)+1):
        if p[0] % 2 == 0:
            p = [make_nxt_n(v) for v in p]
        else:
            if p[0] + 1 == p[1]:
                ans = r
                break
            else:
               p = [make_nxt_n(v) for v in p]
    return ans 
