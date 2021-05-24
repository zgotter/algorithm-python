# 성공
# 다른 사람 풀이

def solution(d, budget):
    answer = 0
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)