# 문제명 : 수빈이와 수열
# url : https://www.acmicpc.net/problem/10539

# 해설 (1) - 성공

N, B = int(input()), list(map(int, input().split()))

A = [B[0]]

for i in range(1, N):
    A.append(B[i]*(i+1) - sum(A))

for i in A:
    print(i, end=' ')