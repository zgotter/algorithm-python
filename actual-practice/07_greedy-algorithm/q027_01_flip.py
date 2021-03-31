# 문제명 : 뒤집기
# url : https://www.acmicpc.net/problem/1439

# 직접 풀이 (1)
#  - 성공
#  - 이전 풀이 참고

S = input()
f0, f1 = 0, 0

if S[0] == '1':
    f0 += 1
else:
    f1 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1': # 0 -> 1
            f0 += 1
        else: # 1 -> 0
            f1 += 1

print(min(f0, f1))