# 문제명 : 가장 큰 증가 부분 수열 (GIS, Greatest Increasing Subsequence)
# url : https://www.acmicpc.net/problem/11055

# 해설 (1) - 성공
from copy import deepcopy

N, A = int(input()), list(map(int, input().split()))

# DP[i] : i 까지 왔을 때 합의 최대
#  - ex) A = [1, 100, 2, 50, 60]
#   - DP[0] = max(1)
#   - DP[1] = max(100, 101)
#   - DP[2] = max(2, 3)
#   - DP[3] = max(50, 51, 52, 53)
#   - DP[4] = max(60, 61, 62, 63, 110, 111, 112, 113)
DP = deepcopy(A)

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(A[i] + DP[j], DP[i])

print(max(DP))