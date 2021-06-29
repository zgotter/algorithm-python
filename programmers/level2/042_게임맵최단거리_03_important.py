# 성공
# 상욱이 풀이
# BFS를 활용하여 최단 거리 탐색

def solution(maps):
    answer = -1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = [[0, 0, 1]]
    maps[0][0] = 0
    
    while queue:
        nx, ny, dist = queue.pop(0)
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x == len(maps) -1 and y == len(maps[0]) -1 :
                answer = dist + 1
                break
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]):
                if maps[x][y] == 1:
                    queue.append([x, y, dist+1])
                    maps[x][y] = 0
        if answer != -1:
            break
    
    return answer