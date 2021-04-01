# 문제명 : 행렬
# url : https://www.acmicpc.net/problem/1080

# 해설 (2)
#  - 코드 개선
#  - 성공

N, M = map(int, input().split())

def input_str():
    return [[int(i) for i in input()] for _ in range(N)]

A, B = input_str(), input_str()

def flip(x, y, A):
    for i in range(0, 3):
        for j in range(0, 3):
            A[x+i][y+j] ^= 1 # ^= 1 : XOR 연산 (0->1, 1-> 0)

ans = 0
for i in range(0, N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
            flip(i, j, A)
            ans += 1

print(-1 if A != B else ans)