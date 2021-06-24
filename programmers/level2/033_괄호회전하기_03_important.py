# 성공
#  - chk() 함수 로직 변경 (올바른 괄호 확인 함수)
#  - "([{)}]" 처리 할 수 있도록 변경
#    - (ASIS) 여는 괄호 등장 시 +1, 닫는 괄호 등장 시 -1
#    - (TOBE) stack 활용!!

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
    lst = [s[i:n] + (s[0:i] if i != 0 else '') for i in range(n)]
    return sum([chk(l) for l in lst])