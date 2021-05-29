# 실패

def get_max_pos(acc, tp):
    m, p = 0, -1
    for i in range(4):
        if acc[i][0] > m:
            m = acc[i][0]
            p = acc[i][1]
    return m if tp == 'm' else p
    

def solution(land):
    acc = [(0,0) for _ in range(4)]
    pos = -1
    for row in land:
        _row = [row[i] if i != pos else 0 for i in range(4)]
        for i in range(4):
            lst = [_row[j] if j != i else 0 for j in range(4)]
            m = max(lst)
            acc[i] = (acc[i][0]+m, _row.index(m))
        pos = get_max_pos(acc, 'p')
        #print(acc, pos)
    ans = get_max_pos(acc, 'm')
    return ans