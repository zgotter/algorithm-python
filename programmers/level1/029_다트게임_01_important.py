# 성공
# 정규표현식 사용

import re

def applyBonus(games, scores):
    pb = re.compile('[SDT]{1}')
    bonus = [pb.findall(game)[0] for game in games]
    for i in range(3):
        if bonus[i] == 'S':
            scores[i] **= 1
        elif bonus[i] == 'D':
            scores[i] **= 2
        else:
            scores[i] **= 3
    return scores

def applyOption(games, scores):
    po = re.compile('[*#]*')
    options = []
    for game in games:
        ol = po.findall(game)
        ol = [o for o in ol if o != '']
        if len(ol) > 0:
            options.append(ol[0])
        else:
            options.append('')
    
    for i in range(3):
        if options[i] == '*':
            scores[i] *= 2
            if i > 0:
                scores[i-1] *= 2
        elif options[i] == '#':
            scores[i] *= -1
    return scores

def solution(dartResult):
    answer = 0
    p = re.compile('[01]*[0-9]{1}[SDT]{1}[*#]*')
    games = p.findall(dartResult)
    
    pn = re.compile('[01]*[0-9]{1}')
    scores = [int(pn.findall(game)[0]) for game in games]
    scores = applyBonus(games, scores)
    scores = applyOption(games, scores)

    return sum(scores)
