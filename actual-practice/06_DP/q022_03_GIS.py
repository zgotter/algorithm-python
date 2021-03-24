# 문제명 : 가장 큰 증가 부분 수열 (GIS, Greatest Increasing Subsequence)
# url : https://www.acmicpc.net/problem/11055

# 해설 (2)
#  - 심화 : 가장 큰 증가 부분 수열을 출력
from copy import deepcopy

N, A = int(input()), list(map(int, input().split()))

# DP[i] : i 까지 왔을 때 합의 최대
DP = deepcopy(A)
# rev : DP의 해당 인덱스의 최대 합이 현재값에 어떤 인덱스의 DP 값이 더해졌는 지가 저장됨
rev = [i for i in range(N)]
# idx : 가장 큰 부분수열의 합을 갖는 DP의 인덱스
idx = 0

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and DP[i] < A[i] + DP[j]:
            DP[i] = A[i] + DP[j]
            rev[i] = j

    if DP[idx] < DP[i]:
        idx = i

print(idx, DP[idx])

# result : 최대 합을 갖는 부분수열
result = []
while rev[idx] != idx:
    result.append(A[idx])
    idx = rev[idx]

result.append(A[idx])
result.reverse()
print(result)