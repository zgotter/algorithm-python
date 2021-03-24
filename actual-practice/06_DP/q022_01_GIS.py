# 문제명 : 가장 큰 증가 부분 수열 (GIS, Greatest Increasing Subsequence)
# url : https://www.acmicpc.net/problem/11055

# 직접 풀이 (1) - 풀이 실패...

N = int(input())
A = list(map(int, input().split()))
DP = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            DP[i] += DP[j]
        DP[j] = 0

print(max(DP))