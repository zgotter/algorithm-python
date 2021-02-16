# 문제명 : Z
# url : https://www.acmicpc.net/problem/1074

# 해설 (1) - 성공

N, r, c = map(int, input().split())

# Z : (0,0)을 기준으로 x, y의 숫자
def Z(sz, x, y):
    if sz == 1: # N = 0
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1): # 첫 번째 칸(왼쪽 상단)
                return (i*2+j) * sz*sz + Z(sz, x - sz*i, y - sz*j)
                # i*2+j
                #  - (0,0) / i=0, j=0 / 0 * 2 + 0 = 0 (i*2+j)
                #  - (0,1) / i=0, j=1 / 0 * 2 + 1 = 1 (i*2+j)
                #  - (1,0) / i=1, j=0 / 1 * 2 + 0 = 2 (i*2+j)
                #  - (1,1) / i=1, j=1 / 1 * 2 + 1 = 3 (i*2+j)

                # sz*sz : 사각형 1개의 크기 (N*N)

print(Z(2**N, r, c))