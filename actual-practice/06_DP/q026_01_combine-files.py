# 문제명 : 파일 합치기
# url : https://www.acmicpc.net/problem/11066

# 해설 (1)
#  - 성공
#  - DP로 구현

def process():
    N, A = int(input()), [0] + list(map(int, input().split()))

    # S[i] : 1번 부터 i번까지의 누적합
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]

    # DP[i][j] : i에서 j까지 합하는 데 필요한 최소 비용
    # DP[i][j] = DP[i][k] + DP[k+1][j] + sum(A[i], ..., A[j])
    # 위의 합이 최소가 되게 하는 k를 찾는 것이 중요하다.
    DP = [[0 for i in range(N+1)] for _ in range(N+1)]
    for i in range(2, N+1): # 부분 파일의 길이 기준 반복문 실행
        for j in range(1, N+2-i): # 시작점 기준 반복문 실행
            # DP[j][j+k] : j에서 k만큼 떨어진 지점까지의 합
            # DP[j+k+1][j+i-1] : DP[j][j+k] 의 다음 지점 부터 마지막 지점 까지의 합
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])

    print(DP[1][N])

for _ in range(int(input())):
    process()