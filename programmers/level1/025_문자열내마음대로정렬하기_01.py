# 성공

def solution(strings, n):
    answer = []
    order_lst = [(s[n], s) for s in strings]
    order_lst.sort()
    for o in order_lst:
        answer.append(o[1])
    return answer