# 성공

from itertools import combinations

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
def solution(nums):
    answer = 0
    for x, y, z in combinations(nums, 3):
        if is_prime(x+y+z): answer += 1
    return answer