# 문제명 : Z
# url : https://www.acmicpc.net/problem/1074

# 직접 풀이 (1) - 시간초과
#  - 유형별 문제 풀이 참고

def solve(n, x, y):
    global result

    if n == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1
        if x == r and y+1 == c:
            print(result)
            return
        result += 1
        if x+1 == r and y == c:
            print(result)
            return
        result += 1
        if x+1 == r and y+1 == c:
            print(result)
            return
        result += 1
        return
    
    halfN = n/2
    solve(halfN, x, y)
    solve(halfN, x, y+halfN)
    solve(halfN, x+halfN, y)
    solve(halfN, x+halfN, y+halfN)

N, r, c = map(int, input().split())

result = 0

solve(2**N, 0, 0)