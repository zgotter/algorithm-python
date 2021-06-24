# 성공
#  - 한칸씩 이동하는 로직 다른 방법 시도 (다른 사람 풀이 참고)

def chk(s):
    stack = []
    o, c = ['(', '{', '['], [')', '}', ']']
    for ss in s:
        if ss in o:
            stack.append(ss)
        elif ss in c:
            if stack:
                if o.index(stack[-1]) == c.index(ss):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    return True
            

def solution(s):
    n = len(s)
    res = []
    for i in range(n):
        res.append(chk(s))
        s = s[1:] + s[0]
    return sum(res)