# 문제명 : 배열 돌리기 4
# url : https://www.acmicpc.net/problem/17406

# 직접 풀이 (1) - 풀이 실패...
from copy import deepcopy
from itertools import permutations



N, M, K = map(int, input().split())

#A = [list(map(int, input().split())) for _ in range(N)]
A = [[0 for _ in range(M+2)]  for _ in range(N+2)]
for i in range(1, N+1):
    row = list(map(int, input().split()))
    row = [0] + row + [0]
    for j in range(1, M+1):
        A[i][j] = row[j]

for a in A:
    print(a)

O = [list(map(int, input().split())) for _ in range(K)]

def rotate(A, r, c, s):
    print(r, ', ', c, ', ', s)
    X = deepcopy(A)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == r-s and j > c-s:
                X[i][j] = A[i][j-1]
    return X

print('----------------')

for kList in permutations(O):
    for r, c, s in kList:
        A = rotate(A, r, c, s)
        break
    break

for a in A:
    print(a)