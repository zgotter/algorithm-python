# 성공

def solution(s, n):
    lst = list(s)
    res = []
    for l in lst:
        if l == ' ': res.append(' ')
        else:
            no = ord(l)+n
            if l == l.lower():
                if no > ord('z'):
                    no = no - ord('z') + ord('a') - 1
                res.append(chr(no))
            else:
                if no > ord('Z'):
                    no = no - ord('Z') + ord('A') - 1
                res.append(chr(no))
    print(res)
    return ''.join(res)