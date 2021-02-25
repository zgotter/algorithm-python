# 문제명 : 꽃길
# url : https://www.acmicpc.net/problem/14620

# 직접 풀이 (2) - 성공
#  - 직접 풀이 (1) 개선
#    - 비용이 적은 순으로 3개를 심는 것이 아니라, 심을 수 있는 모든 위치들에서 3개를 조합으로 뽑아서 모든 경우의 총 비용을 계산
#    - 해당 총 비용들 중에서 가장 작은 값을 결과로 출력

from itertools import combinations

N = int(input())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

prices = [list(map(int, input().split())) for _ in range(N)]

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

result = 10000
for costs_lst in combinations(costs, 3):
    temp_result = 0
    planted = [[False] * N for _ in range(N)]
    for cost in costs_lst:
        already_planted = False
        i, j = cost[0], cost[1]

        for k in range(4):
            ii, jj = i + dx[k], j + dy[k]
            if planted[ii][jj]:
                already_planted = True
                break 

        if already_planted:
            temp_result = 10000
        else:
            planted[i][j] = True
            for k in range(4):
                ii, jj = i + dx[k], j + dy[k]
                planted[ii][jj] = True
            temp_result += cost[2]
    
    result = min(result, temp_result)

print(result)