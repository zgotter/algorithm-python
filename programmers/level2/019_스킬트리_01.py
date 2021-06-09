# 일부 테스트 케이스 실패

def solution(skill, skill_trees):
    answer = 0
    chk = {s: False for s in skill}
    for skill_tree in skill_trees:
        isOk = True
        for s in skill_tree:
            if s not in chk.keys():
                continue
            for k in chk.keys():
                if k != s:
                    if chk[k]:
                        continue
                    else:
                        isOk = False
                        break
                else:
                    chk[k] = True
        if isOk:
            answer += 1
                
    return answer