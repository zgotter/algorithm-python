# 일부 테스트 케이스 실패 (실패, 런타임 에러)

import re

def solution(files):
    p = re.compile('([a-zA-Z.-]+)([\d]{1,5})([\d\sa-zA-Z.-]*)')
    ans = [p.findall(file)[0] for file in files]
    ans.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(a) for a in ans]