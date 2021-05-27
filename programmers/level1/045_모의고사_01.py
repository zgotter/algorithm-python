# 성공

def solution(answers):
    p, res = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]], [0, 0, 0]
    for i, ans in enumerate(answers):
        for j in range(3):
            res[j] += 1 if p[j][i%len(p[j])] == ans else 0
    return [i+1 for i in range(3) if res[i] == max(res)]