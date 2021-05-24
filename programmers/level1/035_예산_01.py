# 실패
# 테스트 케이스 실패 및 시간 초과

from itertools import combinations

def solution(d, budget):
    answer = 0
    d.sort()
    found = False
    for i in range(len(d), 0, -1):
        if not found:
            for lst in combinations(d, i):
                if sum(list(lst)) == budget:
                    answer = len(lst)
                    found = True
                    break
    return answer

print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4