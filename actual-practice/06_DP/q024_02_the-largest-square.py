# 문제명 : 가장 큰 정사각형
# url : https://www.acmicpc.net/problem/1915

# 해설 (1)
#  - 성공

N, M = map(int, input().split())
A = [[0 for _ in range(M+1)] for _ in range(N+1)]
DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for idx, j in enumerate(input()):
        if j == '\r': continue
        A[i+1][idx+1] = int(j)

# DP[i][j]
#  - (i,j) 까지 왔을 때 가장 큰 정사각형의 한 변의 길이
#  - DP[i][j] = min(왼쪽의 DP, 대각선의 DP, 위쪽의 DP) + 1
# DP[i][j]
#  - if A[i][j] == 1 ; DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1 
#  - if A[i][j] == 0 ; DP[i][j] = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i][j] == 1:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
        else:
            DP[i][j] = 0 # 이미 0으로 초기화 되어 있으므로 안 써도 됨

print(max([max(i) for i in DP])**2)