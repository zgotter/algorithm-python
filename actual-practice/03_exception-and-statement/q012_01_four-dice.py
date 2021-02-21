# 문제명 : 주사위 네개
# url : https://www.acmicpc.net/problem/2484

# 직접 풀이 (1) - 성공

N = int(input())

max_price = 0

def get_cnt(a):
    cnt = 0
    for l in lst:
        if a == l:
            cnt += 1
    return cnt

for _ in range(N):
    lst = sorted(list(map(int, input().split())))
    price = 0
    if len(set(lst)) == 1: # (4)
        price = 50000 + lst[0]*5000
    elif len(set(lst)) == 2: # (3,1) or (2,2)
        if lst[1] == lst[2]: # (3,1)
            price = 10000 + lst[1]*1000
        else:
            price = 2000 + lst[0] * 500 + lst[2] * 500
    elif len(set(lst)) == 3: # (2,1,1)
        for i in list(set(lst)):
            if get_cnt(i) == 2:
                price = 1000 + i*100
                break
    else: # (1,1,1,1)
        price = lst[3] * 100
    #print(price)
    max_price = max(price, max_price)

print(max_price)