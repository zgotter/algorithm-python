# 03
#  - gcd 여러 가지 방법으로 구현

def gcd1(x,y):
    v = x
    while v > 1:
        if x % v == 0 and y % v == 0:
            break
        else:
            v -= 1
    return v

def gcd2(x,y):
    for i in range(min(x,y),0,-1):
        if x % i == 0 and y % i == 0: return i

def gcd3(x,y):
    return gcd3(y, x%y) if x % y != 0 else y

def solution(w,h):
    answer = w*h
    x, y = min(w,h), max(w,h)
    g = gcd3(x,y)
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