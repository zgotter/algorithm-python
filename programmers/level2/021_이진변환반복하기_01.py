# 성공

def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        org_len = len(s)
        s = ''.join([a for a in s if a == '1'])
        new_len = len(s)
        answer[1] += org_len-new_len
        s = bin(new_len)[2:]
    return answer