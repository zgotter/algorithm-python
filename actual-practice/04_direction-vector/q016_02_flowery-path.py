# 문제명 : 꽃길
# url : https://www.acmicpc.net/problem/14620

# 해설 (1) - 성공

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

ans = 10000

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0] # 기본적인 방향 벡터에 가만히 있는 것((0,0)) 추가

def ck(lst): # 꽃이 a, b, c에 있을 때의 비용
    ret = 0 # 총 비용
    flow = [] # 위치들, 이 위치들을 중복 제거한 갯수가 15개 일 때 모든 위치에 3개의 꽃이 정상적으로 심어졌다고 판단
    for flower in lst:
        # ex) 2x2 좌표평면의 각 좌표의 x, y값 구하기 (N=2)
        #  - flower = 0; x = 0 // 2 = 0 | y = 0 % 2 = 0 | -> (0,0)
        #  - flower = 1; x = 1 // 2 = 0 | y = 1 % 2 = 1 | -> (0,1)
        #  - flower = 2; x = 2 // 2 = 1 | y = 2 % 2 = 0 | -> (1,0)
        #  - flower = 3; x = 3 // 2 = 1 | y = 3 % 2 = 1 | -> (1,1)
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1: # 화단을 벗어나는 경우
            return 10000
        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += G[x+dx[w]][y+dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret

# 모든 좌표평면의 점을 0 ~ N*N-1 로 표현
# ex) N=2 (-> N*N-1 = 2*2-1 = 3)
#  - [[0,1],[2,3]]
for i in range(N*N): 
    for j in range(N*N):
        for k in range(N*N):
            ans = min(ans, ck([i, j, k]))

print(ans)