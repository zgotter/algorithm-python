# 성공

def solution(arr):
    answer = []
    prev = ''
    for a in arr:
        if a != prev:
            answer.append(a)
            prev = a
    return answer