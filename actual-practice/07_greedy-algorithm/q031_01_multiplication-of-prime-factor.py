# 문제명 : 소수의 곱
# url : https://www.acmicpc.net/problem/2014

# 직접 풀이 (1)
#  - 예제는 성공
#  - 제출 시 시간 초과 발생

from collections import defaultdict

K, N = map(int, input().split())
P = [int(i) for i in input().split()]

# 소인수 분해 함수
def get_prime_factor(num):
    dic = defaultdict(int)
    d = 2
    while d <= num:
        if num % d == 0:
            dic[d] += 1
            num = num/d
        else:
            d += 1
    return list(dic.keys())

cnt = 0
now_num = 1
while True:
    if cnt == N:
        break
    now_num += 1
    p_list = get_prime_factor(now_num)
    chk = True
    for p in p_list:
        if p not in P:
            chk = False
            break
    if chk:
        cnt += 1
    
print(now_num)