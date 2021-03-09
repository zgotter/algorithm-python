# 2차원 배열 회전
#  - 참고 : https://shoark7.github.io/programming/algorithm/rotate-2d-array

from copy import deepcopy

N = 3

val = 1
B = []
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(val)
        val += 1
    B.append(tmp)

for b in B:
    print(b)

print('------------------------')

# 오른쪽으로 90도 회전 (왼쪽으로 270도 회전과 동일)
#  - 회전 후 행 번호 : 회전 전 열 번호와 동일
#  - 회전 후 열 번호 : N-1에서 회전 전 행 번호를 뺀 값 (N-1 : out of index 방지)

def rotate_right_90(B):
    tempB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            tempB[j][N-i-1] = B[i][j]
    return tempB

NB90 = rotate_right_90(B)
for b in NB90: print(b)

print('------------------------')

# 오른쪽으로 180도 회전 (왼쪽으로 180도 회전과 동일)
#  - 회전 후 행 번호 : N-1에서 회전 전 행 번호를 뺀 값
#  - 회전 후 열 번호 : N-1에서 회전 전 열 번호를 뺀 값

def rotate_right_180(B):
    tempB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            tempB[N-1-i][N-1-j] = B[i][j]
    return tempB

NB180 = rotate_right_180(B)
for b in NB180: print(b)

print('------------------------')

# 오른쪽으로 270도 회전 (왼쪽으로 90도 회전과 동일)
#  - 회전 후 행 번호 : N-1에서 회전 전 열 번호를 뺀 값
#  - 회전 후 열 번호 : 회전 전 행 번호와 동일

def rotate_right_270(B):
    tempB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            tempB[N-1-j][i] = B[i][j]
    return tempB

NB270 = rotate_right_270(B)
for b in NB270: print(b)