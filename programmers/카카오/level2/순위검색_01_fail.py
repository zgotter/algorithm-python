# 효율성 테스트 실패

def solution(info, query):
    answer = []
    info = [i.split(' ') for i in info]
    for q in query:
        q_list = q.split(' and ')
        q_list = q_list[:-1] + q_list[-1].split(' ')
        now_info = info
        for i in range(4):
            if q_list[i] != "-":
                now_info = [n_i for n_i in now_info if n_i[i] == q_list[i]]
        now_info = [n_i for n_i in now_info if int(n_i[-1]) >= int(q_list[-1])]
        answer.append(len(now_info))
    return answer