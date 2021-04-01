# 문제명 : 저울
# url : https://www.acmicpc.net/problem/2437

# 해설 (1)
#  - 성공

"""
1: 1
2: 1+1, 2
3: 1+2
4: 1+1+2
5: 2+3
6: 6
7: 7
8: 7+1
...
13: 6+7
14: 6+1+7
"""
# 1부터 6까지 만들 수 있다면, 7부터 13까지 만들 수 있다.
# 이전 상태까지 만들 수 있는 무게 S가 있을 때, 그 다음 무게 N가 한 칸 크거나 같으면(S >= N+1)
# 계속 쌓아나아 갈 수 있다.


N, A = int(input()), sorted(list(map(int, input().split())))

# ans : 만들 수 있는 최소값
ans = 0
for i in A:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans+1)