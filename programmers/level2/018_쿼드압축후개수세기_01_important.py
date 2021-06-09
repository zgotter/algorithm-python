# 다른 사람 풀이
# 이중배열 좌표 재귀 (recursive)

def comp(arr, x, y, n, ans):
    init = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            nv = arr[i][j]
            if nv != init:
                nn = n//2
                comp(arr, x, y, nn, ans)
                comp(arr, x, y+nn, nn, ans)
                comp(arr, x+nn, y, nn, ans)
                comp(arr, x+nn, y+nn, nn, ans)
                return
    ans[init] += 1
                
def solution(arr):
    ans = [0,0]
    N = len(arr)
    comp(arr, 0, 0, N, ans)
    return ans

print()
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))