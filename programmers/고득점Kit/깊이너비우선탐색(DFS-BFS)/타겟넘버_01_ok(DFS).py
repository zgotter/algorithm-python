# 성공
# DFS를 이용한 풀이

answer = 0

def dfs(idx, result, numbers, target):
    global answer
    if idx == len(numbers):
        if result == target:
            answer += 1
    else:
        dfs(idx + 1, result + numbers[idx], numbers, target)
        dfs(idx + 1, result - numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer