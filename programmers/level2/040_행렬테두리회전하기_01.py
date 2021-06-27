# 성공

def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    n = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j] = n
            n += 1
    for x1, y1, x2, y2 in queries:
        x, y = x1, y1
        tmp = arr[x][y]
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        move_cnt = [y2-y1, x2-x1, y2-y1, x2-x1]
        lst = []
        for i in range(4):
            for _ in range(move_cnt[i]):
                xx, yy = x + dx[i], y + dy[i]
                tmp2 = arr[xx][yy]
                lst.append(tmp)
                arr[xx][yy] = tmp
                tmp = tmp2
                x, y = xx, yy
        answer.append(min(lst))
    return answer