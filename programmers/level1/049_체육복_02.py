# 다른 사람 풀이

def solution(n, lost, reserve):
    sr = set(reserve) - set(lost)
    sl = set(lost) - set(reserve)
    for r in sr:
        if r-1 in sl:
            sl.remove(r-1)
        elif r+1 in sl:
            sl.remove(r+1)
    return n - len(sl)

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2