# 문제명 : 수 찾기
# url : https://www.acmicpc.net/problem/1920

# 해설 - 성공
# - 딕셔너리 활용, 3항 연산자 활용

N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input() # 필요없는 입력 무시

for i in list(map(int, input().split())):
    print(1 if i in A else 0) # 3항 연산자