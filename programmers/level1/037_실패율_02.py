# 성공
# 분모의 값이 0이 되는 경우를 고려해야 했음

def solution(N, stages):
    fail_rate_lst = []
    for i in range(1, N+1):
        a = len([s for s in stages if s == i])
        b = len([s for s in stages if s >= i])
        fail_rate_lst.append((i, (a/b if b != 0 else 0)))
    fail_rate_lst.sort(key=lambda x:x[1], reverse=True)
    return [x[0] for x in fail_rate_lst]