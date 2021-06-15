# 실패 (시간초과)

from itertools import combinations

def solution(number, k):
    ans = []
    lst = list(number)
    for a in combinations(lst, len(number)-k):
        val = ''.join(a)
        if len(ans) == 0 or max(ans) < val:
            ans.append(val)
    print(ans)
    return max(ans)