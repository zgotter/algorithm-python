# 문제명 : 수빈이와 수열
# url : https://www.acmicpc.net/problem/10539

# 직접 풀이 - 성공

n = int(input())
b = list(map(int, input().split()))

a = [0] * n

for i in range(n):
    val = (i+1) * b[i]
    if i > 0:
        val -= sum(a[:i])
    a[i] = val

print(' '.join(map(str, a)))