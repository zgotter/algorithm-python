# 정확성 테스트 케이스 1개 실패 (시간초과)

def solution(arr):
    if len(arr) <= 1: return [-1]
    return [i for i in arr if i != min(arr)]