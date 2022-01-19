# 실패 (테스트 케이스 25번 실패)

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
                    if costs[nx][ny] >= cost + new_cost: # > -> >=
                        costs[nx][ny] = cost + new_cost
                        queue.append([nx, ny, cost + new_cost, directions[i]])
                        
    return costs[n-1][n-1]


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
    print(solution(board))