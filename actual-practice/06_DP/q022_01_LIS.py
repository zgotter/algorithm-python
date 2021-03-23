# 문제명 : 가장 큰 증가 부분 수열
# url : https://www.acmicpc.net/problem/11055

# 직접 풀이 (1)

N = int(input())
A = list(map(int, input().split()))

print(A)

result = 0
tmp = 0
for i in range(N):
    if A[i] < A[i+1]:
        pass
