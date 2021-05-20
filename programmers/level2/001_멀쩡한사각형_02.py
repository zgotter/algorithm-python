# 02 - 성공
#  - gcd 구현

def gcd(x,y):
    v = x
    while v > 1:
        if x % v == 0 and y % v == 0:
            break
        else:
            v -= 1
    return v

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