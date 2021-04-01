# 문제명 : 행렬
# url : https://www.acmicpc.net/problem/1080

# 직접 풀이 (1)

N, M = map(int, input().split())
A = [[int(i) for i in input()] for _ in range(N)]
B = [[int(i) for i in input()] for _ in range(N)]

for a in A:
    print(a)

print('----------')

for b in B:
    print(b)