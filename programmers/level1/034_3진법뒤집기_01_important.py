# 성공
# 10진수 -> n진수
# n진수 -> 10진수 : int(n진수값, n) -> 10진수값 리턴

import string

# 10진수 -> n진수 변경 함수
tmp = string.digits + string.ascii_lowercase
def convert10ton(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert10ton(q, base) + tmp[r]

def convert10ton2(num, base):
    res = []
    while num > 0:
        num, r = divmod(num, base)
        res.append(str(r))
    return ''.join(reversed(res))

def solution(n):
    answer = convert10ton2(n, 3)
    answer = answer[::-1]
    print(type(answer))
    answer = int(answer,3) # n -> 10
    print(type(answer))
    return answer

print(solution(45))