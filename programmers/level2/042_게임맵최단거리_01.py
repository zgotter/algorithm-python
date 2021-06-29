# 실패
# 다른 사람 풀이 참고

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y]
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0 and maps[xx][yy] == 1: # yy < n -> yy < m 수정 필요
                visited[xx][yy] = visited[x][y] + 1
                queue.append((xx, yy))
    return -1