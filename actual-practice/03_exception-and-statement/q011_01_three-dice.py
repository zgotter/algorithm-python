# 문제명 : 주사위 세개
# url : https://www.acmicpc.net/problem/2480

# 직접 풀이 (1) - 성공

lst = list(map(int, input().split()))

lst_unique = list(set(lst))

def get_cnt(a):
    cnt = 0
    for l in lst:
        if a == l:
            cnt += 1
    return cnt

if len(lst_unique) == 1:
    print(10000 + lst_unique[0] * 1000)
elif len(lst_unique) == 2:
    for u in lst_unique:
        if get_cnt(u) == 2:
            print(1000 + u * 100)
            break
elif len(lst_unique) == 3:
    print(max(lst_unique) * 100)
