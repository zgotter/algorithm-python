# 성공

def solution(a, b):
    answer = ''
    mday = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    cnt = b-1
    for i in range(1, a):
        cnt += mday[i-1]
    return day[cnt%7]