# 일부 테스트 케이스 실패

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def get_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs(arr, x, y):
    res = True
    visited = [[False for _ in range(5)] for _ in range(5)]
    queue = deque([(x, y, "")])
    visited[x][y] == True
    
    while queue:
        xx, yy, temp = queue.popleft()
        dist = get_dist(x, y, xx, yy)
        if dist >= 3:
            continue
        elif dist == 1:
            if arr[xx][yy] == "P":
                res = False
                break
        elif dist == 2:
            if temp == "O" and arr[xx][yy] == "P":
                res = False
                break

        for i in range(4):
            xxx, yyy = xx + dx[i], yy + dy[i]
            if 0 <= xxx < 5 and 0 <= yyy < 5 and not visited[xxx][yyy]:
                visited[xxx][yyy] = True
                temp2 = arr[xxx][yyy] if dist == 1 else ""
                queue.append((xxx, yyy, temp2))
    return res
    
def check(arr):
    persons = [(x, y) for x in range(5) for y in range(5) if arr[x][y] == "P"]
    for person in persons:
        x, y = person
        result = bfs(arr, x, y)
        if not result:
            return 0
    return 1
    

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer