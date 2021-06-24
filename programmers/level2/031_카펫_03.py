# 성공
# brown 을 이용해서 모양을 찾아야 함

def get_divisor(n): # 약수 구하기
    return [i for i in range(1, n//2+1) if n % i == 0] + [n]

def solution(brown, yellow):
    answer = [0, 0]
    for n in get_divisor(yellow):
        m = yellow // n
        if n >= m:
            x, y = n+2, m+2
            if x * y - yellow == brown:
                answer = [x, y]
                break
    return answer