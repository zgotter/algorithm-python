# 성공 (복습)

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    
    (x1, y1), (x2, y2) = pos
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        xx1, yy1 = x1 + dx[i], y1 + dy[i]
        xx2, yy2 = x2 + dx[i], y2 + dy[i]
        if board[xx1][yy1] == 0 and board[xx2][yy2] == 0:
            next_pos.append(set([(xx1, yy1), (xx2, yy2)]))
    
    if x1 == x2:
        for nx in [-1, 1]:
            xx1 = x1 + nx
            xx2 = x2 + nx
            if board[xx1][y1] == 0 and board[xx2][y2] == 0:
                next_pos.append(set([(x1, y1), (xx1, y1)]))
                next_pos.append(set([(x2, y2), (xx2, y2)]))
    
    if y1 == y2:
        for ny in [-1, 1]:
            yy1 = y1 + ny
            yy2 = y2 + ny
            if board[x1][yy1] == 0 and board[x2][yy2] == 0:
                next_pos.append(set([(x1, y1), (x1, yy1)]))
                next_pos.append(set([(x2, y2), (x2, yy2)]))
    
    return next_pos

def solution(board):
    answer = 0
    n = len(board)
    
    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    visited = []
    queue = deque([])
    
    pos = set([(1, 1), (1, 2)])
    visited.append(pos)
    queue.append((pos, 0))
    
    while queue:
        new_pos, move = queue.popleft()
        
        if (n, n) in new_pos:
            answer = move
            break
        
        for next_pos in get_next_pos(new_pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                queue.append((next_pos, move+1))
    
    return answer