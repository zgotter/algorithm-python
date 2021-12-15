# 실패

def is_valid_str(s):
    lst = []
    for ss in s:
        if ss == "(":
            lst.append(ss)
        elif ss == ")":
            if len(lst) == 0 or lst[-1] != "(":
                return False
            lst.pop()
    return True if len(lst) == 0 else False
            
def split_str(s):
    cnt = 0
    for i in range(len(s)):
        cnt += 1 if s[i] == "(" else -1
        if cnt == 0:
            return s[:i+1], s[i+1:]

def solution(p):
    answer = ''
    if not p:
        return answer
    if is_valid_str(p):
        return p
    
    while True:
        u, v = split_str(p)
        if is_valid_str(u):
            answer += u
            p = v
            continue
        else:
            answer += "(" + v + ")" + "".join(["(" if uu == ")" else ")" for uu in u[1:-1]])
            break
        
    return answer