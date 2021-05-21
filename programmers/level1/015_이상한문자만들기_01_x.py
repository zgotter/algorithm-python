# 테스트 케이스 일부 실패
# 맞는 거 같은데...
def solution(s):
    res = []
    for l in list(s.split()):
        tmp = ''
        for idx, v in enumerate(l):
            tmp += v.upper() if idx % 2 == 0 else v.lower()
        res.append(tmp)
    return ' '.join(res)

print(0 % 2)