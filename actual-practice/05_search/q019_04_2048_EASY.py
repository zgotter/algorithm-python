# 문제명 : 2048 (Easy)
# url : https://www.acmicpc.net/problem/12100

# 복습 (1) - 성공

from copy import deepcopy

def convert(l):
    ll = [i for i in l if i > 0]
    for i in range(len(ll)-1):
        if ll[i] == ll[i+1]:
            ll[i], ll[i+1] = ll[i]*2, 0
    ll = [i for i in ll if i > 0]
    return ll + [0] * (len(l) - len(ll))

def rotate(A, N):
    X = deepcopy(A)
    for i in range(N):
        for j in range(N):
            X[N-1-j][i] = A[i][j]
    return X

def dfs(A, s, N):
    ret = max([max(i) for i in A])
    if s == 0: return ret

    for _ in range(4):
        X = [convert(x) for x in A]
        if A != X: ret = max(ret, dfs(X, s-1, N))
        A = rotate(A, N)
    return ret

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

print(dfs(B, 5, N))