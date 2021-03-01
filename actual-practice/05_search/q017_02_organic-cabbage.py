# 문제명 : 유기농 배추
# url : https://www.acmicpc.net/problem/1012

# 직접 풀이 (2) - 성공 
#  - (주의) 입력 조건에서 가로 세로 별 입력 조건이 주어질 때 다음을 주의해야 한다.
#    - 세로 : 행
#    - 가로 : 열
#  - 코드 개선
#    1) M, N 변수 가로, 세로 제대로 표현하도록 변경 
#    2) lst 변수에 배추가 심어져 있는 좌표를 따로 저장하지 않고, 
#       모든 좌표를 돌며 배추가 심어져 있는 경우에만 dfs 를 실행하도록
#       로직 변경
#    3) field, visited 변수 dfs 함수 파라미터에서 제외

T = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    global bugCnt
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if field[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    bugCnt = 0
    
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    for x in range(N):
        for y in range(M):
            if field[x][y] and not visited[x][y]:
                dfs(x, y)
                bugCnt += 1
    
    print(bugCnt)