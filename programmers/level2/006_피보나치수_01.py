# 일부 테스트 케이스 실패 (런타임 에러, 시간초과)
# 재귀 함수 사용

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

def solution(n):
    return fibo(n) % 1234567