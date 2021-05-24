# 성공

from copy import deepcopy

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = deepcopy(array)
        arr = arr[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer