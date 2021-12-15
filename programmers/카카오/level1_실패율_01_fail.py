# 실패 (런타임 에러)

def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        fail_ratio = len([s for s in stages if s == i]) / len([s for s in stages if s >= i])
        answer.append((i, fail_ratio))
    answer = sorted(answer, key=lambda x: -x[1])
    answer = [ans for ans, _ in answer]
    return answer