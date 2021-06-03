# 성공
# 이전 풀이 참고
# 동적계획법 (DP, 다이나믹 프로그래밍)

def solution(board):
    x, y = len(board), len(board[0])
    b = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    
    for i in range(x):
        for j in range(y):
            b[i+1][j+1] = board[i][j]
            
    for i in range(1, x+1):
        for j in range(1, y+1):
            if b[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
    return max([max(d) for d in dp])**2
        