# 성공

def solution(skill, skill_trees):
    answer = 0
    lst = [skill[:i] for i in range(1, len(skill)+1)]
    for st in skill_trees:
        sub = ''.join([s for s in st if s in skill])
        if sub == '' or sub in lst:
            answer += 1
    return answer