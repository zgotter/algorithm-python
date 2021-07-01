# 성공
# 복습
# deque 사용한 BFS 활용

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        acc, idx = queue.popleft()
        if idx == len(numbers):
            if acc == target:
                answer += 1
        else:
            num = numbers[idx]
            queue.append((acc + num, idx + 1))
            queue.append((acc - num, idx + 1))
    return answer