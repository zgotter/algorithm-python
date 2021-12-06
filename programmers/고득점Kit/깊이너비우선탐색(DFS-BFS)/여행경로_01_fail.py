# 테스트 케이스 1, 2 실패

from collections import deque

def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))]
    queue = deque(["ICN"])
    while queue:
        city = queue.popleft()
        answer.append(city)
        targets = [[idx, ticket] for idx, ticket in enumerate(tickets) if not visited[idx] and ticket[0] == city]
        targets = sorted(targets, key=lambda x: x[1][1])
        if targets:
            idx, ticket = targets[0]
            visited[idx] = True
            queue.append(ticket[1])
    return answer