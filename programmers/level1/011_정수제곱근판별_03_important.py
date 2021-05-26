# 성공
    
def solution(n):
    s = n ** (1/2) # 제곱근 구하기
    return int((s+1)**2) if int(s) == s else -1

print(solution(121))
print(solution(3))