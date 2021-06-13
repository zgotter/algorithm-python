# 성공
# 코드 개선

def solution(n):
    directs = [[1,0], [0,1], [-1,-1]]
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y, val = 0, 0, 1
    for i in range(n):
        cnt = n-i
        idx = i % len(directs)
        for j in range(cnt):
            arr[x][y] = val
            val += 1
            idx = idx if j != cnt-1 else (idx + 1) % len(directs)
            x = x + directs[idx][0]
            y = y + directs[idx][1]
    return [v for a in arr for v in a if v != 0]