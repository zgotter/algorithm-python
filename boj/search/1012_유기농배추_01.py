def dfs(arr, n, m, visited, x, y):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited[x][y] = True
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if arr[xx][yy] == 1 and visited[xx][yy] == False:
            dfs(arr, n, m, visited, xx, yy)

testCase = int(input())

for _ in range(testCase):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    res = 0
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
    #print(arr)
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                res += 1
                dfs(arr, n, m, visited, i, j)    
    print(res)
