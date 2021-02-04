# 문제명 : 이름 궁합 테스트
# url : https://www.acmicpc.net/problem/17269

# 복습 - 성공 (123004 KB, 112 ms)

strokes = [
    3, 2, 1, 2, 4,
    3, 1, 3, 1, 1,
    3, 1, 3, 2, 1,
    2, 2, 2, 1, 2,
    1, 1, 1, 2, 2, 1
]

N, M = map(int, input().split())
A, B = input().split()

minLength = min(N, M)

AB = ''
for i in range(minLength):
    AB += A[i] + B[i]

AB += A[minLength:] + B[minLength:]

lst = [strokes[ord(i) - ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print('{}%'.format(lst[0] % 10 * 10 + lst[1] % 10))