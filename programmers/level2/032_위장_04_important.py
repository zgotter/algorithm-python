# 성공
# 다른 사람 풀이 참고
# 공식 활용
#  - ex) 상의=1개, 하의=2개, 얼굴=3개
#    - 모든 경우의 수 = (1+1) x (2+1) x (3+1) - 1 = 23
# 딕셔너리 직접 생성 대신 Counter 클래스 활용

from collections import Counter

def solution(clothes):
    dic = Counter([kind for name, kind in clothes])
    ans = 1
    for v in dic.values():
        ans *= (v+1)
    ans -= 1
    return ans