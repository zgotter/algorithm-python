# 성공
# BFS를 이용한 풀이

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0)) # idx, accumulate
    while queue:
        idx, acc = queue.popleft()
        if idx == len(numbers):
            if acc == target:
                answer += 1
        else:
            queue.append((idx+1, acc + numbers[idx]))
            queue.append((idx+1, acc - numbers[idx]))
    return answer