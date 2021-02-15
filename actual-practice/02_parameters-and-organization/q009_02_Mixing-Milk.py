# 문제명 : Mixing Milk
# url : https://www.acmicpc.net/problem/16769

# 해설 (1) - 성공

C, M = list(), list()

for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx = i % 3
    nxt = (idx + 1) % 3 ###
    # M[idx] : "현재 잔의 우유량 - 다음 잔에 옮길 수 있는 우유량" vs "0" 중 큰 값
    # M[nxt] : "다음 잔에 최대로 채울 수 있는 우유량" vs "현재 잔의 우유량 + 다음 잔의 우유량" 중 작은 값
    # 한 줄로 써줘야 동시에 변화가 된다!!
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)