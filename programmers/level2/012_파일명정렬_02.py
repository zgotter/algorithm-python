# 성공

import re

def solution(files):
    p = re.compile('([a-zA-Z\s.-]+)([\d]{1,5})([\da-zA-Z\s.-]*)')
    ans = [p.findall(file)[0] for file in files]
    ans.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(a) for a in ans]