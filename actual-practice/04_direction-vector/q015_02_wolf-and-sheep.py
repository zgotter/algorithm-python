# 문제명 : 늑대와 양
# url : https://www.acmicpc.net/problem/16956

# 해설 (1) - 성공

R, C = map(int, input().split())
M = [list(input()) for i in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ck = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4):
                ii, jj = i + dx[w], j + dy[w]
                if ii < 0 or ii == R or jj < 0 or jj == C:
                    continue
                if M[ii][jj] == 'S': # W 상하좌우에 S가 있으면 늑대가 양이 있는 칸으로 갈 수 있다.
                    ck = True

if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW': # '.' 으로 되어 있는 부분에 모두 울타리(D)로 채우기
                M[i][j] = 'D'

for i in M:
    print(''.join(i))