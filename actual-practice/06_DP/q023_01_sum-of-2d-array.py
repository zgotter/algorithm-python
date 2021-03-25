# 문제명 : 2차원 배열의 합
# url : https://www.acmicpc.net/problem/2167

# 직접 풀이 (1) - 풀이 실패

def process(i, j, x, y):
    print(i, j, x, y)

N, M = map(int, input().split())
A = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, M+1):
        A[i][j] = tmp[j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    process(i, j, x, y)