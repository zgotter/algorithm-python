# 실패 (일부 테스트 케이스 런타임 에러 발생)

def solution(N, stages):
    fail_rate_lst = []
    for i in range(1, N+1):
        a = len([s for s in stages if s <= i and s >= i])
        b = len([s for s in stages if s >= i])
        fail_rate_lst.append((i, a/b))
    fail_rate_lst.sort(key=lambda x:x[1], reverse=True)
    return [x[0] for x in fail_rate_lst]