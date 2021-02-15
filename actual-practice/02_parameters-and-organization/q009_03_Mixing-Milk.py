# 문제명 : Mixing Milk
# url : https://www.acmicpc.net/problem/16769

# 해설 (2) - 성공
#  - 코드 간소화

C, M = [0, 0, 0], [0, 0, 0]

for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    idx, nxt = i % 3, (i+1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)