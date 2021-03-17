# 문제명 : 배열 돌리기 4
# url : https://www.acmicpc.net/problem/17406

# 복습 (2) - 성공
#  - 백트래킹 사용
from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dr, dc = [1, 0, -1, 0], [0, -1, 0, 1]

ans = 10000

def get_arr_min(arr):
    return min([sum(i) for i in arr])

def convert(arr, qry):
    r, c, s = qry
    r = r-1
    c = c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr+dr[w], cc+dc[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr


def dfs(arr, qry):
    global ans
    if sum(qry) == K:
        ans = min(ans, get_arr_min(arr))
        return

    for i in range(K):
        if qry[i]: continue
        new_arr = convert(arr, Q[i])
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0
    

dfs(A, [0 for _ in range(K)])
print(ans)