# 문제명 : 수 찾기
# url : https://www.acmicpc.net/problem/1920

# 해설 - 성공
# - 딕셔너리 활용, 딕셔너리 get 메서드 활용

N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input() # 필요없는 입력 무시

for i in list(map(int, input().split())):
    # dict.get(key, default)
    #  - 딕셔너리에 key값에 해당하는 value가 있는 지 확인
    #  - 있으면 해당 value 리턴
    #  - 없으면 default 값 리턴
    print(A.get(i, 0))