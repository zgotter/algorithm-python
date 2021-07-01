# 정확성 테스트 6개(3~8) 실패 (시간 초과)
# 효율성 테스트 8개(1~8) 실패 (시간 초과)

def solution(s):
    answer = -1
    lst = list(s)
    while True:
        chk = False
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                chk = True
                lst = lst[:i] + lst[i+2:]
                break
        if chk == False:
            answer = 0
            break
        if len(lst) == 0:
            answer = 1
            break
        
    return answer