# 문제명 : APC는 왜 서브태스크 대회가 되었을까?
# url : https://www.acmicpc.net/problem/17224

# 복습 - 140점

N, L, K = map(int, input().split()) # N: 문제의 갯수, L: 역량(난이도 기준), K: 풀 수 있는 문제의 최대 개수

easy, hard = 0, 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

scores = 0
# 어려운 버전 해결 : 쉬운 버전(100)과 어려운 버전 모두 해결로 +140
scores += min(hard, K)*140

if hard < K: 
    # 쉬운 버전과 어려운 버전 모두를 해결한 문제의 수가 풀 수 있는 문제의 수보다 적은 경우
    # 즉, 풀 수 있는 문제의 수가 남은 경우
    # 풀 수 있는 남은 문제의 갯수 이하로만 쉬운 버전의 문제를 해결할 수 있다.
    scores += min(K-hard, easy)*100
        
print(scores)
