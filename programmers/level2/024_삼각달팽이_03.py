# 성공
# 코드 개선 (2)

def solution(n):
    dx, dy = [1, 0, -1], [0, 1, -1]
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y, val = 0, 0, 1
    for i in range(n):
        cnt = n-i
        idx = i % 3
        for j in range(cnt):
            arr[x][y] = val
            val += 1
            idx = idx if j != cnt-1 else (idx + 1) % 3
            x = x + dx[idx]
            y = y + dy[idx]
    return [v for a in arr for v in a if v != 0]