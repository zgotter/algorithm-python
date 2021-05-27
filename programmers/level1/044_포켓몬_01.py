# 성공

def solution(nums):
    halfN = int(len(nums)/2)
    unique = list(set(nums))
    return halfN if len(unique) > halfN else len(unique)