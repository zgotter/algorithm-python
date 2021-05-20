# 01 - 성공
#  - gcd 라이브러리 사용

from math import gcd

def solution(w,h):
    answer = w*h
    x, y = min(w,h), max(w,h)
    g = gcd(x,y)
    xx, yy = x//g, y//g
    l, cnt = 0, 0
    while True:
        l += xx
        if l < yy:
            cnt += 1
        elif l > yy:
            cnt += 2
            l -= yy
        else:
            cnt += 1
            break
    return answer - (cnt * g)

print(solution(8,12))