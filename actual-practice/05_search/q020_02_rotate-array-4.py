# 문제명 : 배열 돌리기 4
# url : https://www.acmicpc.net/problem/17406

# 해설 (1) - 성공
#  - permutation 대신 백트래킹(DFS 활용, 전수조사) 를 활용
#   - 파이썬에서 permutation을 사용하면 튜플 형태로 반환되며 사용하기 조금 복잡할 수 있다.

#  - query를 처리하는 방법으로 리스트 활용

#  - query를 처리하는 방법으로 '비트 마스크 기법' 사용할 수 있다.
#   - 쿼리의 값들 중 어떤 값을 처리했는 지 체크하는 기법
#    - (방법 1) 반복문으로 탐색 -> 시간 복잡도 = O(N^2) (비효율적)
#    - (방법 2) set() 사용 -> 시간 복잡도 O(N^2) (비효율적)
#    - (방법 3) 비트 마스크 기법 (bitmask)
#     - 쿼리의 각각의 원소를 이진수로 변환
#     - 시간 복잡도 = O(N)
#     - 체크 배열을 이진수로 변환한 것

from copy import deepcopy

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 남, 서, 북, 동

# 배열의 각 행의 합 중 최소값을 반환하는 함수
def value(arr): 
    return min([sum(i) for i in arr])

ans = 10000


def convert(arr, qry):
    # 원소 회전 방법
    #  1) 중앙에서 오른쪽 대각선 끝 원소 탐색
    #  2) 오른쪽 방향으로 진행하며 원소 변경
    r, c, s = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)

    for i in range(1, s+1): # i : 중심에서부터 떨어진 거리
        rr, cc = r-i, c+i # 출발 지점 (중앙에서 오른쪽 대각선 끝 원소)
        for w in range(4): # 방향을 4번 바꿈 (아래(남), 왼쪽(서), 위(북), 오른쪽(동))
            for d in range(i*2): # 하나의 방향에서 이동할 칸의 갯수 
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc

    return new_arr

def dfs(arr, qry):  # qry :  각 쿼리의 처리 결과를 0과 1로 표현 (0: 미처리, 1: 처리)
    global ans
    if sum(qry) == K:
        ans = min(ans, value(arr))
        return

    for i in range(K):
        if qry[i]: # qry[i] == 1
            continue
        new_arr = convert(arr, Q[i]) # i번 째 쿼리를 이용하여 배열 변환
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0 # 백트래킹 기법

dfs(A, [0 for i in range(K)])

print(ans)