# 문제명 : 2차원 배열의 합
# url : https://www.acmicpc.net/problem/2167

# 해설 (1)
# - 성공

# - 핵심 아이디어 : 누적합 구하기, 교집합 빼기

# - 1차원 배열의 누적합
#  - DP[i] = i까지의 합
#  - i 부터 j 까지의 합 : DP[i] - DP[j-1]

# - 2차원 배열의 누적합
#  - (i,j) 부터 (x,y) 까지의 누적합
#   = (x,y)의 왼쪽에서의 누적합 + (x,y)의 위쪽에서의 누적합 - (x,y)의 왼쪽 대각선에서의 누적합 + 현재값
#   = (x-1,y)까지의 누적합 + (x,y-1)까지의 누적합 - (x-1,y-1)까지의 누적합 + 현재값

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# DP[i][j] : (1,1) 부터 (i,j) 까지의 부분합
DP = [[0 for i in range(M+1)] for _ in range(N+1)]

# 2차원 배열의 누적합 구하기
for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]

# (i,j) 부터 (x,y) 까지의 부분합 구하기
#  - 이미지 참고 : https://claude-u.tistory.com/303
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])