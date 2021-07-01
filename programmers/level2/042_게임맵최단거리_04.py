# 일부 테스트 케이스 실패
# 복습

from collections import deque

def solution(maps):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    distances = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0)])
    distances[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            return distances[x][y]
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and maps[xx][yy] == 1: # yy < n --> yy < m 으로 수정 필요!!!!!!
                if distances[xx][yy] == 0:
                    distances[xx][yy] = distances[x][y] + 1
                    queue.append((xx, yy))
    return -1