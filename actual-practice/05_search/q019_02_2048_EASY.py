# 문제명 : 2048 (Easy)
# url : https://www.acmicpc.net/problem/12100

# 해설 (1) - 성공
#  - 삼성 코딩 테스트에서 해당 문제와 비슷한 유형의 문제 출제됨
#  - 이와 같은 문제는 시간 복잡도를 고려했을 때, python 보다는 java 로 푸는 게 좋다.
#  - 4가지 방향을 모두 탐색하는 것이 아니라, B 를 한 가지 방향으로 돌리는 식으로 접근하는 것이 좋다.
#    - 위로 슬라이드 : B를 왼쪽으로 90도 회전 후 왼쪽으로 모두 이동
#    - 오른쪽으로 슬라이드 : B를 왼쪽으로 180도 회전 후 왼쪽으로 모두 이동
#    - 아래로 슬라이드 : B를 왼쪽으로 270도 회전 후 왼쪽으로 모두 이동

from copy import deepcopy

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

def rotate90(B, N): # B를 왼쪽으로 90도 회전
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[N-1-j][i] = B[i][j] # 90도 회전 (2dArrayRotate.py 참고)
    return NB

def convert(lst, N): # 왼쪽 방향으로 슬라이드
    new_lst = [i for i in lst if i > 0] # 0이 아닌 숫자만 남기기
    for i in range(1, len(new_lst)): # 현재 값 : N; N-1 == N -> N = 0, N-1 = (N-1)*2
        if new_lst[i-1] == new_lst[i]:
            new_lst[i-1] *= 2
            new_lst[i] = 0
    new_lst = [i for i in new_lst if i > 0]
    return new_lst + [0] * (N-len(new_lst))

def dfs(N, B, count):
    ret = max([max(i) for i in B])

    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(x, N) for x in B] ##
        if X != B: # 회전한 결과가 원래의 B와 동일하지 않은 경우만 진행
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)
    
    return ret

print(dfs(N, B, 5))