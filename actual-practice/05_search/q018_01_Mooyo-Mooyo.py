# 문제명 : Mooyo Mooyo
# url : https://www.acmicpc.net/problem/16768

# 해설 (1) - 성공
# - Flood Fill(플러드 필)
# - 2차원 배열 내부 요소 이동

# 1) 그룹을 찾고 그룹의 원소의 갯수 반환 (DFS, BFS 이용)
# 2) 그룹의 원소의 갯수가 K 이상일 때 해당 원소 삭제
# 3) 삭제 후 나머지 값들을 아래로 이동

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)
ck2 = new_array(N)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10: # 범위 체크
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret

def dfs2(x, y, val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10: # 범위 체크
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)

def down():
    for i in range(10): # 세로별로
        tmp = []
        for j in range(N):
            if M[j][i] != '0': # 0이 아닌 값들 tmp 에 임시 저장
                tmp.append(M[j][i])
        for j in range(N-len(tmp)): # tmp의 길이를 제외한 나머지를 0으로 채움
            M[j][i] = '0'
        for j in range(N-len(tmp), N): # tmp에 있는 값들을 하나 씩 채움
            M[j][i] = tmp[j - (N-len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j) # 그룹 내 원소의 갯수 카운트 (res : 그룹의 총 크기)
            if res >= K:
                dfs2(i, j, M[i][j]) # 지우기
                exist = True

    if not exist:
        break
    down() # 삭제 후 나머지 원소 아래로 이동

for i in M:
    print(''.join(i))