# 문제명 : The candy war
# url : https://www.acmicpc.net/problem/9037

# 직접 풀이 (1) - 성공

T = int(input())

def makeEven(N, C):
    for i in range(N):
        if C[i] % 2 != 0:
            C[i] += 1

def check(N, C):
    val = C[0]
    for i in range(1, N):
        if not val == C[i]:
            return False
    return True

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    makeEven(N, C)

    cycle = 0
    while not check(N, C):
        half = [c//2 for c in C]
        C = [c//2 for c in C]
        C[0] += half[-1]
        for i in range(1, N):
            C[i] += half[i-1]
        
        makeEven(N, C)
        cycle += 1
    
    print(cycle)
