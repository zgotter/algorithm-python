# 성공
# 복습

import re

def solution(dartResult):
    c1 = re.compile('[1-9]*[0-9]+[SDT]+[*#]*')
    lst = c1.findall(dartResult)
    
    c2 = re.compile('[1-9]*[0-9]+')
    scores = [int(c2.findall(l)[0]) for l in lst]
    
    areas = [1 if 'S' in l else (2 if 'D' in l else 3) for l in lst]
    scores = [score**a for score, a in zip(scores, areas)]
    
    for i, l in enumerate(lst):
        if l[-1] == '*':
            scores[i] *= 2
            if i > 0:
                scores[i-1] *= 2
        elif l[-1] == '#':
            scores[i] *= -1
            
    return sum(scores)
