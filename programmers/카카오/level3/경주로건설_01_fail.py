# dfs로 시도... 실패

from collections import deque

n = None

def bfs(board, x, y):
    global n
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우
    directions = ["vertical", "vertical", "horizontal", "horizontal"]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True
    queue = deque([(x, y, 0, "")])
    costs = []
    while queue:
        xx, yy, cost, before_direction = queue.popleft()
        print(xx, yy)
        if xx == n-1 and yy == n-1:
            costs.append(cost)
        else:
            for i in range(4):
                nx, ny = xx + dx[i], yy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not board[nx][ny]:
                    visited[nx][ny] = True
                    new_cost = cost
                    if before_direction == "":
                        new_cost = cost + 100
                    elif before_direction == directions[i]:
                        new_cost = cost + 100
                    else:
                        new_cost = cost + 500
                    queue.append((nx, ny, new_cost, directions[i]))
    
    print(costs)
    

def solution(board):
    global n
    
    answer = 0
    n = len(board)
    bfs(board, 0, 0)
    return answer