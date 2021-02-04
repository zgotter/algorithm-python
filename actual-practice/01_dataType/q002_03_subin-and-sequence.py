# 문제명 : 수빈이와 수열
# url : https://www.acmicpc.net/problem/10539

# 해설 (2) - 성공
#  - A 리스트를 미리 선언하므로서 append 대신 리스트 배열에 값을 바꿔주는 식으로 변경
#  - 양이 많아질 때 속도 개선의 효과를 얻을 수 있음

N, B = int(input()), list(map(int, input().split()))

A = [0 for i in range(N)]
A[0] = B[0]

for i in range(1, N):
    A[i] = (B[i]*(i+1) - sum(A))

for i in A:
    print(i, end=' ')
