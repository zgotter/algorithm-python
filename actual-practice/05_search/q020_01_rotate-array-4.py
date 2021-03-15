# 문제명 : 배열 돌리기 4
# url : https://www.acmicpc.net/problem/17406

# 직접 풀이 (1) - 

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
O = [list(map(int, input().split())) for _ in range(K)]

for a in A:
    print(a)

print(O)