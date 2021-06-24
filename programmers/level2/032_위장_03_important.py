# 성공
# 다른 사람 풀이 참고
# 공식 활용
#  - ex) 상의=1개, 하의=2개, 얼굴=3개
#    - 모든 경우의 수 = (1+1) x (2+1) x (3+1) - 1 = 23

def solution(clothes):
    dic = dict()
    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
    ans = 1
    for v in dic.values():
        ans *= (v+1)
    ans -= 1
    return ans