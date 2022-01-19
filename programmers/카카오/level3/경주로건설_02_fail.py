# 테스트 1, 3, 4 성공 / 2 실패 (시간 초과)
# dfs 활용
# 무한루프 확인 필요
import sys
sys.setrecursionlimit(10000)

n = None
costs = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우
directions = ["vertical", "vertical", "horizontal", "horizontal"]

def dfs(board, visited, x, y, cost, direction):
    global n, costs, dx, dy, directions
    
    if x == n-1 and y == n-1:
        costs.append(cost)
        return
    
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and not board[xx][yy]:
            visited[xx][yy] = True
            new_cost = 100 if direction == "" or direction == directions[i] else 600
            dfs(board, visited, xx, yy, cost + new_cost, directions[i])
            visited[xx][yy] = False
    
    

def solution(board):
    global n, costs
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    dfs(board, visited, 0, 0, 0, "")
    
    print(costs)
    
    return min(costs)


if __name__ == "__main__":
    board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
    print(solution(board))