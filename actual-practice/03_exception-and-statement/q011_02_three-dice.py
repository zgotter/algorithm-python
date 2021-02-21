# 문제명 : 주사위 세개
# url : https://www.acmicpc.net/problem/2480

# 해설 (1) - 성공

lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
    print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
    # 3개 중 2개가 같은 값 이라면 크기순으로 정렬했을 때, 중간 값이 값이 2개인 수가 된다.
    print(1000 + lst[1] * 100)
else:
    # 3개가 모두 다른 값이라면 크기순으로 정렬했을 때, 마지막 값이 가장 큰 수가 된다.
    print(lst[2] * 100)