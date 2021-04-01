# 문제명 : 근우의 다이어리 꾸미기
# url : https://www.acmicpc.net/problem/16676

# 해설 (1)
#  - 성공

# 1 ~ 10 : 1
# 11 ~ 110 : 2
# 111 ~ 1110 : 3

N = input()
S = '1'*len(N) # 1, 11, 111, 1111, ...

if len(N) == 1:
    print(1)
elif int(N) >= int(S):
    print(len(N))
else:
    print(len(N)-1)
