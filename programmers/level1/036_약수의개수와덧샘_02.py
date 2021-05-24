# 성공
# 코드 간소화

def get_divisor_cnt(n):
    cnt = 0
    for i in range(n//2):
        if n % (i+1) == 0:
            cnt += 1
    return cnt+1

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        answer += n * (1 if get_divisor_cnt(n) % 2 == 0 else -1)
    return answer