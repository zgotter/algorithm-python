# 성공
# while문 탈출 조건 수정

def solution(citations):
    answer = 0
    n = len(citations)
    h = 0
    while True:
        if h > len(citations): break # 이 부분 수정
        lst = [c for c in citations if c >= h]
        if len(lst) >= h:
            answer = h
        h += 1
    return answer