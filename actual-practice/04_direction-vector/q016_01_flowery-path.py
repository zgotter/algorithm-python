# 문제명 : 꽃길
# url : https://www.acmicpc.net/problem/14620

# 직접 풀이 (1) - 실패
#  - 예제 입력은 성공
#  - 제출 시 실패 (틀렸습니다)

N = int(input())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

prices = []

for _ in range(N):
    prices.append(list(map(int, input().split())))

# 1. 각 지점 당 꽃을 심을 수 있는 경우의 비용 계산
costs = []

for i in range(N):
    for j in range(N):
        check = True
        cost = prices[i][j]
        for k in range(4):
            ii, jj = i+dx[k], j+dy[k]
            if ii < 0 or ii == N or jj < 0 or jj == N:
                check = False
                break
            cost += prices[ii][jj]
        if check:
            costs.append((i, j, cost))

# 2. 비용 오름차순 정렬
costs = sorted(costs, key = lambda x: x[2])

# 3. 비용이 적은 위치부터 꽃을 심을 수 있는 위치 3개 탐색
flower_cnt = 0 # 현재까지 심은 꽃의 수
result = 0
planted = [[False] * N for _ in range(N)]

for cost in costs:
    if flower_cnt == 3:
        break
    i, j = cost[0], cost[1]
    already_planted = False
    
    for k in range(4):
        ii, jj = i + dx[k], j + dy[k]
        if planted[ii][jj]:
            already_planted = True
            break
    
    if not already_planted:
        planted[i][j] = True
        for k in range(4):
            ii, jj = i + dx[k], j + dy[k]
            planted[ii][jj] = True
        flower_cnt += 1
        result += cost[2]

print(result)
    