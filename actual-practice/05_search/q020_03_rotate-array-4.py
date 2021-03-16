# 문제명 : 배열 돌리기 4
# url : https://www.acmicpc.net/problem/17406

# 복습 (1) - 성공
#  - 해설 (1) 에서 permutation 사용
#  - dfs를 활용한 것 보다 많은 시간이 소요됨

from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 남, 서, 북, 동

def arr_min(arr): 
    return min([sum(i) for i in arr])

def convert(arr, qry):
    r, c, s = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc

    return new_arr

ans = 10000
for qList in permutations(Q):
    new_arr = deepcopy(A)
    for q in qList:
        new_arr = convert(new_arr, q)
    ans = min(ans, arr_min(new_arr))

print(ans)