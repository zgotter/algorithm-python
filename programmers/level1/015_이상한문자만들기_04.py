# 성공 풀이 참고 코드 개선
#  - 각 단어를 리스트에 담아서 변경하니 성공함

def solution(s):
    w_lst = s.split(' ')
    for k in range(len(w_lst)):
        nw_lst = list(w_lst[k])
        for i in range(len(nw_lst)):
            nw_lst[i] = nw_lst[i].upper() if i % 2 == 0 else nw_lst[i].lower()
        w_lst[k] = ''.join(nw_lst)
    return ' '.join(w_lst)

print(solution("try hello world"))