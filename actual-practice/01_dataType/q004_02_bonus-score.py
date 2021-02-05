# 문제명 : 보너스 점수
# url : https://www.acmicpc.net/problem/17389

# 해설 (1) - 성공 (122244 KB, 104 ms)

N, S = int(input()), input()

score, bonus = 0, 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx+1+bonus
        bonus += 1
    else:
        bonus = 0

print(score)