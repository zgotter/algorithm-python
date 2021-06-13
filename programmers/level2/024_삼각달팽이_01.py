# 성공

def solution(n):
    answer = []
    directs = [[1,0], [0,1], [-1,-1]]
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y, val = 0, 0, 1
    for i in range(n):
        cnt = n-i
        d_idx = i % len(directs)
        for j in range(cnt):
            arr[x][y] = val
            val += 1
            d_idx = d_idx if j != cnt-1 else (d_idx + 1) % len(directs)
            x, y = x + directs[d_idx][0], y + directs[d_idx][1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0: answer.append(arr[i][j])
    return answer