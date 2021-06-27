# 1개 테스트 케이스(9번) 실패

def solution(citations):
    answer = 0
    n = len(citations)
    h = 0
    while True:
        if h == len(citations): break
        lst = [c for c in citations if c >= h]
        if len(lst) >= h:
            answer = h
        h += 1
    return answer