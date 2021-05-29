# 성공

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            #land[i][j] += max([l for k, l in enumerate(land[i-1]) if k != j])
            land[i][j] += max([land[i-1][k] for k in range(4) if k != j])
    return max(land[len(land)-1])