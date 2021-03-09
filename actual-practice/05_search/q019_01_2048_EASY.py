# 문제명 : 2048 (Easy)
# url : https://www.acmicpc.net/problem/12100

# 직접 풀이 (1) - 

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def move(direction):
    pass


max_val = max(map(max, M)) # 2차원 배열 최댓값
for _ in range(5):
    for i in range(4):
        move(i)
    