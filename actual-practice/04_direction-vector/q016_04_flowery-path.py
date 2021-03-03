# 문제명 : 꽃길
# url : https://www.acmicpc.net/problem/14620

# 복습 (1) - 성공

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
min_cost = 10000

def get_cost(lst):
    cost = 0
    planted = []
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000
        for w in range(5):
            nx, ny = x + dx[w], y + dy[w]
            planted.append((nx, ny))
            cost += G[nx][ny]
    if len(set(planted)) != 15:
        return 10000
    return cost

for i in range(N*N):
    for j in range(N*N):
        for k in range(N*N):
            min_cost = min(min_cost, get_cost([i, j, k]))

print(min_cost)