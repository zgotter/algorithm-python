# 문제명 : APC는 왜 서브태스크 대회가 되었을까?
# url : https://www.acmicpc.net/problem/17224

# 해설 (1) - 140점

N, L, K = map(int, input().split())

easy, hard = 0, 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# hard 문제
ans = min(hard, K) * 140 

# easy 문제
if hard < K: # 어려운 버전을 푼 문제를 제외하고 더 풀 수 있는 문제의 갯수가 남은 경우(쉬운 문제만 해결한 경우)
    ans += min(K-hard, easy) * 100

print(ans)