# 성공

def solution(n):
    w = ['수','박']
    answer = ''
    for i in range(n):
        answer += w[i%2]
    return answer