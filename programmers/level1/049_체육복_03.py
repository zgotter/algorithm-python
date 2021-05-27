# 다른 사람 풀이

def solution(n, lost, reserve):
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
    for r in _reserve:
        a, b = r-1, r+1
        if a in _lost: _lost.remove(a)
        elif b in _lost: _lost.remove(b)
    return n - len(_lost)

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
