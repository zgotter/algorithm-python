# 정확성 테스트 케이스 18번 실패

def solution(n):
    answer = 0
    x = 2
    while True:
        xx = x**2
        if xx > n:
            answer = -1
            break
        if n == x**2:
            answer = (x+1)**2
            break
        x += 1
        
    return answer