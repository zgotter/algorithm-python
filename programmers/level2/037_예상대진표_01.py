# 일부 테스트 케이스 실패

def get_max_r(n):
    r = 0
    while n > 1:
        n = n // 2
        r += 1
    return r

def solution(n,a,b):
    r = 0
    max_r = get_max_r(n)
    while True:
        r += 1
        if r == max_r:
            break
        if (a+1) % 2 == 0 and (a+1) == b:
            break
        aa = a if a % 2 == 0 else a+1
        bb = b if b % 2 == 0 else b+1
        a = aa // 2
        b = bb // 2
    return r