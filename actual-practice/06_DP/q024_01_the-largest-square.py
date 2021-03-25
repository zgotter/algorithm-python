# 문제명 : 가장 큰 정사각형
# url : https://www.acmicpc.net/problem/1915

# 직접 풀이 (1)
#  - 풀이 실패

N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    row = input()
    for j in range(M):
        A[i][j] = int(row[j])

for a in A:
    print(a)