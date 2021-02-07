# 문제명 : 수 찾기
# url : https://www.acmicpc.net/problem/1920

# 직접 풀이 - 성공

N, A= int(input()), list(map(int, input().split()))
M, V = int(input()), list(map(int, input().split()))

for v in V:
    if v in A:
        print(1)
    else:
        print(0)
