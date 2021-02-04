# 문제명 : 이름 궁합 테스트
# url : https://www.acmicpc.net/problem/17269

# 해설 (1) - 성공 (123004 KB, 108 ms)

N, M = map(int, input().split())
A, B = input().split()

alp = [
    3, 2, 1, 2, 4,
    3, 1, 3, 1, 1,
    3, 1, 3, 2, 1,
    2, 2, 2, 1, 2,
    1, 1, 1, 2, 2, 1
]

AB = ''
# 먼저 길이가 짧은 이름 기준으로 문자열 만들기
min_len = min(N, M)
for i in range(min_len):
    AB += A[i] + B[i]

# 남은 이름 문자열에 붙이기
AB += A[min_len:] + B[min_len:]

# ord() 함수를 이용해 각 알파벳 인덱스 생성 (A:0, B:1, C:2, ...)
lst = [alp[ord(i) - ord('A')] for i in AB]

# 궁합 구하기 작업 수행
for i in range(N+M-2): # 두 이름의 길이의 합 - 2 만큼 반복
    for j in range(N+M-1-i): # 두 이름의 길이의 합에서 1을 뺀 값에 현재 수행되는 횟수의 인덱스를 차감한 만큼 반복
        lst[j] += lst[j+1]

print('{}%'.format(lst[0] % 10*10 + lst[1] % 10))