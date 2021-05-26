# 성공
# 복습

def solution(n):
    a = n ** (1/2)
    return int((a+1)**2) if int(a) == a else -1

print(solution(121))
print(solution(3))