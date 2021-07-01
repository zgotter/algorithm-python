# 문제명 : 배열 돌리기 4
# url : https://www.acmicpc.net/problem/17406

# 복습 (3) - 성공
#  - permutations 사용

from copy import deepcopy
from itertools import permutations

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dr, dc = [1, 0, -1, 0], [0, -1, 0, 1]

def get_arr_min(arr):
    return min([sum(i) for i in arr])

def convert(arr, qry):
    r, c, s = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dr[w], cc + dc[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr

ans = 10000
for qList in permutations(Q):
    new_arr = deepcopy(A)
    for q in qList:
        new_arr = convert(new_arr, q)
    ans = min(ans, get_arr_min(new_arr))

print(ans)