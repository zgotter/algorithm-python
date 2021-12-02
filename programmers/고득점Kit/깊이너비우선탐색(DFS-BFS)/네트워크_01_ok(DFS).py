# 성공

def dfs(computers, n, visited, idx):
    visited[idx] = True
    for j in range(n):
        if not visited[j] and computers[idx][j] == 1:
            dfs(computers, n, visited, j)
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(computers, n, visited, i)
            answer += 1 # 연결된 모든 컴퓨터를 방문하는 dfs를 수행하면 하나의 네트워크가 생긴 것이다.
    return answer