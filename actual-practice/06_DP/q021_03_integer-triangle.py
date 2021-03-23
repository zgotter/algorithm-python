# 문제명 : 정수 삼각형
# url : https://www.acmicpc.net/problem/1932

# 해설 (1) - 성공

N = int(input())

# 첫 번째 열에 0을 채워 인덱스가 1부터 시작하도록 한다.
A = [[0 for _ in range(N+1)] for _ in range(N+1)]
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        A[i][j] = tmp[j-1]

# DP 식
#  - DP[i][j] : i, j 도착했을 때 최댓값
#  - DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]
for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]

print(max(DP[-1]))