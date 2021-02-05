# 문제명 : 보너스 점수
# url : https://www.acmicpc.net/problem/17389

# 직접 풀이 - 성공 (122244 KB, 112 ms)

N, S = int(input()), input()

score = 0
bonusScore = 0
for i in range(N):
    if ord(S[i]) == 79: # O
        score += (i+1) + bonusScore
        bonusScore += 1
    else: # X
        bonusScore = 0

print(score)