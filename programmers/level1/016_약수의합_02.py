# 약수를 구할 땐 해당값의 절반 이하만 탐색하면 됨 (시간 줄일 수 있음)
# 성공

def solution(n):
    return sum([i+1 for i in range(n//2) if n % (i+1) == 0] + [n])

