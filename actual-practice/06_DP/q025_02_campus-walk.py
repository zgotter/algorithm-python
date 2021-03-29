# 문제명 : 본대 산책
# url : https://www.acmicpc.net/problem/12849

# 해설 (2)
#  - 성공 (123232 KB, 144 ms)
#  - nxt() 함수를 실행할 때 마다 나머지 연산 실행
#  - 마지막에 한 번 할 때보다 메모리와 시간 모두 감소함
#   - 나눗셈 연산이 상당히 무겁다.

# [정보과학관(0), 전산관(1), 미래관(2), 신앙관(3), 한경직(4), 진리관(5), 학생회관(6), 형남공학관(7)]
# 0분에 어떤 지점에 도착할 수 있는 상태
DP = [1, 0, 0, 0, 0, 0, 0, 0]

# 이전 상태에서 지금 상태(1분 후 상태)로 오는 점화식 함수
def nxt(state):
    tmp = [0 for _ in range(8)]
    tmp[0] = state[1] + state[2] # 정보과학관에 오기 위해서는 전산관 또는 미래관에 1분 전에 도착해야 한다.
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    for i in range(8):
        tmp[i] %= 1000000007
    return tmp

for i in range(int(input())):
    DP = nxt(DP)

print(DP[0]) 