# 성공

def solution(arr1, arr2):
    a, b, c = len(arr1), len(arr2), len(arr2[0])
    ans = [[0 for _ in range(c)] for _ in range(a)]
    
    for i in range(a):
        for j in range(c):
            tmp = 0
            for k in range(b):
                tmp += arr1[i][k] * arr2[k][j]
            ans[i][j] = tmp
    return ans