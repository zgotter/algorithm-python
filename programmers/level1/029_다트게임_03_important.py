# 성공
# 다른 사람 풀이
# 정규표현식 활용
#  - '()' 로 감쌀 경우 각각 출력 된다!

import re

def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T': 3}
    option = {'':1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        #print(dart[i])
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
            
    answer = sum(dart)
    return answer

print(solution('1S2D*3T')) # 37
