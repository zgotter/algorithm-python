def solution(arr1, arr2):
    x, y = len(arr1), len(arr1[0])
    answer = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer