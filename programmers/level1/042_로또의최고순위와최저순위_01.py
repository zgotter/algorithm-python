# 성공

def solution(lottos, win_nums):
    #ranks = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    ranks = [6,6,5,4,3,2,1]
    m_cnt = len(list(set(lottos) & set(win_nums)))
    answer = [ranks[m_cnt+lottos.count(0)], ranks[m_cnt]]
    return answer