# 일부 테스트 케이스(4/13) 실패

def get_divisor(n):
    return [i for i in range(1, n//2+1) if n % i == 0] + [n]

def solution(brown, yellow):
    answer = [0, 0]
    for n in get_divisor(yellow):
        m = yellow // n
        #print(n, m, r)
        if n >= m:
            answer = [n+2, m+2]
            break
    return answer