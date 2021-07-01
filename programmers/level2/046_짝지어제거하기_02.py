# 정확성 테스트 6개(3~8) 실패 (시간 초과)
# 효율성 테스트 8개(1~8) 실패 (시간 초과)

def solution(s):
    answer = -1
    words = [w*2 for w in set(s)]
    while True:
        idx = sorted([s.find(word) for word in words if s.find(word) != -1])
        if len(s) > 0 and len(idx) == 0:
            answer = 0
            break
        i = idx[0]
        s = s[:i] + s[i+2:]
        if len(s) == 0:
            answer = 1
            break
    return answer