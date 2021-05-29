# 성공
# 다른 사람 풀이

def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(r, c)) for c in zip(*arr2)] for r in arr1]

a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];

print(solution(a,b))