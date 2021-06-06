# 성공

def solution(dirs):
    d = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    visited = []
    nx, ny = 0, 0
    ans = 0
    for dir in dirs:
        nnx, nny = nx + d[dir][0], ny + d[dir][1]
        if abs(nnx) > 5 or abs(nny) > 5: continue
        road = [(nx, ny), (nnx, nny)]
        road.sort()
        if road not in visited:
            visited.append(road)
            ans += 1
        nx, ny = nnx, nny
    return ans