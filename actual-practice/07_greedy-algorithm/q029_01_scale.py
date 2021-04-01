# 문제명 : 저울
# url : https://www.acmicpc.net/problem/2437

# 직접 풀이 (1)

N = int(input())
S = list(map(int, input().split()))
S.sort()
print(S)

"""
1: 1
2: 1+1, 2
3: 1+2
4: 1+1+2

"""