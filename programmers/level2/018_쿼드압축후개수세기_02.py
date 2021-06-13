# 복습
# 성공
# 이중배열 좌표 재귀 (recursive)

def comp(ans, arr, x, y, n):
    data = arr[x][y]
    for i in range(x, n+x):
        for j in range(y, n+y):
            if data != arr[i][j]:
                nn = n // 2
                comp(ans, arr, x, y, nn)
                comp(ans, arr, x+nn, y, nn)
                comp(ans, arr, x, y+nn, nn)
                comp(ans, arr, x+nn, y+nn, nn)
                return
    ans[data] += 1

def solution(arr):
    answer = [0, 0]
    comp(answer, arr, 0, 0, len(arr))
    return answer

print()
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))