# 성공

def solution(n):
    ans = 0
    for x in range(1, n+1):
        v, acc = x, 0
        chk = False
        while True:
            acc += v
            if acc == n:
                chk = True
                break
            elif acc > n:
                break
            else:
                v += 1
        if chk:
            ans += 1
    return ans