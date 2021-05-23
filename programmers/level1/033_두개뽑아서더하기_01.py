# 성공
# 조합(Combinations) 라이브러리 사용하여 구현

from itertools import combinations # permutation

def solution(numbers):
    answer = []
    for a, b in combinations(numbers, 2):
        answer.append(a+b)
    answer = list(set(answer))
    answer.sort()
    return answer