# 성공
# 이쁘지 않다...

dx, dy = [0, 0, 1, 1], [0, 1, 0, 1]

def check(m, n, board, x, y):
    if x == (m-1) or y == (n-1):
        return []
    block = board[x][y]
    if block == "-":
        return []
    locations = [(x+dx[i], y+dy[i]) for i in range(4)]
    for xx, yy in locations:
        if board[xx][yy] != block:
            return []
    return locations

def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        # remove
        for i in range(m):
            for j in range(n):
                res = check(m, n, board, i, j)
                if res:
                    for x, y in res:
                        visited[x][y] = True
        
        new_count = sum([1 for i in range(m) for j in range(n) if visited[i][j]])
        if new_count == 0:
            break
            
        answer += new_count
        
        # move
        for j in range(n):
            temp = []
            for i in range(m-1, -1, -1):
                if not visited[i][j]:
                    temp.append(board[i][j])
            temp = temp + ['-' for _ in range(m-len(temp))]
            temp = temp[::-1]
            for i in range(m):
                board[i][j] = temp[i]
        
    return answer