# 실패

def solution(answers):
    answer = []
    ps = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    ans = [[p[i%len(p)] for i in range(len(answers))] for p in ps]
    max_score = 0
    for i, a in enumerate(ans):
        matched = sum([a1 == a2 for a1, a2 in zip(a, answers)])
        if matched >= max_score:
            answer.append(i+1)
            max_score = matched
    answer = sorted(answer)
    return answer