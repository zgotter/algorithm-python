# 다른 사람 풀이 ()
# https://somjang.tistory.com/entry/Programmers-%EC%9D%B4%EC%83%81%ED%95%9C-%EB%AC%B8%EC%9E%90-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python
# - 성공

def solution(s):
    s_split = s.split(' ')
    for k in range(len(s_split)):
        s_list = list(s_split[k])
        for i in range(len(s_list)):
            if i % 2 == 0:
                s_list[i] = s_list[i].upper()
            else:
                s_list[i] = s_list[i].lower()
        s_split[k] = ''.join(s_list)
    answer = ' '.join(s_split)
    return answer

print(solution("try hello world"))