# 성공
# 다른 사람 풀이 참고
# deque 를 사용한 BFS 활용

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0,0)])
    while queue:
        cur_sum, idx = queue.popleft()
        if idx == len(numbers):
            if cur_sum == target:
                answer += 1
        else:
            number = numbers[idx]
            queue.append((cur_sum + number, idx+1))
            queue.append((cur_sum - number, idx+1))
    return answer