# 성공
# 다른 사람 풀이 참고

def solution(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))