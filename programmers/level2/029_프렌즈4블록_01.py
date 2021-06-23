# 테스트 케이스 9번 만 실패..

def find(m, n, board, matched):
    dx, dy = [0, 0, 1, 1], [0, 1, 0, 1]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == 'Z': continue
            isMatch = True
            s = ''
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if s == '':
                    s = board[x][y]
                else:
                    if s != board[x][y]:
                        isMatch = False
                        break
            if isMatch:
                for k in range(4):
                    matched[i+dx[k]][j+dy[k]] = True

def moveDown(m, n, board, matched):
    res = [['Z' for _ in range(n)] for _ in range(m)]
    for i in range(n):
        lst = []
        for j in range(m):
            if not matched[j][i]:
                lst.append(board[j][i])
        for k, j in enumerate(range(m-len(lst), m)):
            res[j][i] = lst[k]
    return res
                

def solution(m, n, board):
    res = 0
    while True:
        matched = [[False for _ in range(n)] for _ in range(m)]
        find(m, n, board, matched)
        cnt = len([1 for mat in matched for m in mat if m])
        if cnt == 0: break
        res += cnt
        board = moveDown(m, n, board, matched)
    return res