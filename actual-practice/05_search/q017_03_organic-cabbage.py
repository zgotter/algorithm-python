# 문제명 : 유기농 배추
# url : https://www.acmicpc.net/problem/1012

# 해설 (1) - 성공
#  - DFS 활용

import sys
sys.setrecursionlimit(10000) # DFS 사용 시 재귀함수의 깊이를 제한하는 로직을 추가해 줘야 한다.

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx, yy)

def process():
    global B, ck
    M, N, K = map(int, input().split())
    # 가로, 세로에 양쪽에 한 줄씩 더해 줌으로서 x,y 인덱스가 0인 것은 탐색 범위를 벗어났다는 것을
    # 쉽게 알 수 있다.
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]

    for _ in range(K):
        Y, X = map(int, input().split())
        B[X+1][Y+1] = 1

    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not B[i][j] or ck[i][j]:
                continue
            dfs(i, j)
            ans += 1
    
    print(ans)

for _ in range(T):
    process()