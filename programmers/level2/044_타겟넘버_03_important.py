# 테스트 케이스 2개(1,2) 실패
# 리스트를 사용한 BFS 활용
# -> BFS 수행 시 리스트 자료구조를 사용하는 것보다 deque 자료구조를 사용하는 것이 시간 복잡도를 줄일 수 있다!

def solution(numbers, target):
    answer = 0
    queue = [(0,0)]
    while queue:
        acc, idx = queue.pop(0)
        if idx == len(numbers):
            if acc == target:
                answer += 1
        else:
            num = numbers[idx]
            queue.append((acc + num, idx+1))
            queue.append((acc - num, idx+1))
    return answer