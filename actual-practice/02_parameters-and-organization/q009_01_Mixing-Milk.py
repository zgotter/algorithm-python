# 문제명 : Mixing Milk
# url : https://www.acmicpc.net/problem/16769

# 직접 풀이 (1) - 성공

C, M = list(), list()
for _ in range(3):
    c, m = map(int, input().split())
    C.append(c)
    M.append(m)

for i in range(100):
    bi = i % 3
    ai = 0 if bi == 2 else bi+1
    val = min(M[bi], C[ai] - M[ai])
    M[bi] -= val
    M[ai] += val

for m in M:
    print(m)