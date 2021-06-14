# 문제명 : 유기농 배추
# url : https://www.acmicpc.net/problem/1012

# 직접 풀이 (1) - 성공

T = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(field, visited, x, y):
    global bugCnt
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if field[nx][ny] and not visited[nx][ny]:
                dfs(field, visited, nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    lst = []
    bugCnt = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
        lst.append((x, y))

    for x, y in lst:
        if not visited[x][y]:
            dfs(field, visited, x, y)
            bugCnt += 1
    
    print(bugCnt)