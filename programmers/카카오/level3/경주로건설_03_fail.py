# 테스트 1, 3, 4 성공 / 2 실패 (오답)
# bfs 활용
# 어느 방향부터 탐색하는지에 따라 답이 달라질 수 있는 듯 하다.

from collections import deque

def solution(board):
    n = len(board)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우
    directions = ["vertical", "vertical", "horizontal", "horizontal"]
    costs = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([[0, 0, 0, ""]])
    while queue:
        x, y, cost, direction = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                new_cost = 100 if direction == "" or direction == directions[i] else 600
                if costs[nx][ny] == 0:
                    costs[nx][ny] = cost + new_cost
                    queue.append([nx, ny, cost + new_cost, directions[i]])
                else:
                    if costs[nx][ny] > cost + new_cost:
                        costs[nx][ny] = cost + new_cost
                        queue.append([nx, ny, cost + new_cost, directions[i]])
                        
    for cost in costs:
        print(cost)
    
    return costs[n-1][n-1]