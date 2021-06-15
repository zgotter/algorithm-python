# 실패 (시간초과)

from itertools import combinations

def solution(number, k):
    ans = []
    lst = list(number)
    for a in combinations(lst, len(number)-k):
        ans.append(''.join(a))
    return max(ans)