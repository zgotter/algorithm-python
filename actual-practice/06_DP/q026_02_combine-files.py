# 문제명 : 파일 합치기
# url : https://www.acmicpc.net/problem/11066

# 해설 (2)
#  - 성공
#  - 재귀로 구현
#   - 더 많은 시간이 소요 된다.

TC = int(input())
S, DP = 0, 0

def f(i, j):
    global S, DP
    if i == j: return 0
    if DP[i][j] != -1: return DP[i][j]
    for k in range(i, j):
        tmp = f(i, k) + f(k+1, j) + S[j] - S[i-1]
        if DP[i][j] == -1 or DP[i][j] > tmp: DP[i][j] = tmp
    return DP[i][j]

def process():
    global S, DP
    N, A = int(input()), list(map(int, input().split()))
    S, DP = [0 for _ in range(N+1)], [[-1 for _ in range(N+1)] for i in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i-1]
    print(f(1, N))

for _ in range(TC):
    process()