# 성공
# 복습

def gcd(x, y):
    return gcd(y, x%y) if x % y != 0 else y

def solution(w,h):
    answer = w*h
    x, y = min(w, h), max(w, h)
    g = gcd(x, y)
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