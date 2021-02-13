# 문제명 : The candy war
# url : https://www.acmicpc.net/problem/9037

# 직접 풀이 (2) - 성공

T = int(input())

def makeEven(N, C):
    for i in range(N):
        if C[i] % 2 != 0:
            C[i] += 1

def check(C):
    return len(set(C)) == 1

def transfer(N, C):
    ret = [c//2 for c in C]
    temp = ret.copy()
    ret[0] += temp[-1]
    for i in range(1, N):
        ret[i] += temp[i-1]
    return ret

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    makeEven(N, C)
    cycle = 0
    while not check(C):
        C = transfer(N, C)
        makeEven(N, C)
        cycle += 1
    print(cycle)
