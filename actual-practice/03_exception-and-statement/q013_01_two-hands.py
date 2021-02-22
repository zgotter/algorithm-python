# 문제명 : 두 개의 손
# url : https://www.acmicpc.net/problem/16675

# 직접 풀이 (1) - 성공

def match(a, b):
    if a == 'R' and b == 'S':
        return 'left'
    if a == 'R' and b == 'P':
        return 'right'
    if a == 'S' and b == 'R':
        return 'right'
    if a == 'S' and b == 'P':
        return 'left'
    if a == 'P' and b == 'S':
        return 'right'
    if a == 'P' and b == 'R':
        return 'left'
    return 'draw'

ml, mr, tl, tr = input().split()

M = [ml, mr]
T = [tl, tr]

win_MS, win_TK = 0, 0
if ml == mr and tl != tr:
    if 'right' in [match(ml, tl), match(ml, tr)]:
        win_TK += 1
elif ml != mr and tl == tr:
    if 'left' in [match(ml, tl), match(mr, tl)]:
        win_MS += 1
else:
    for i in range(2):
        for j in range(2):
            result = match(M[i], T[j])
            if result == 'left':
                win_MS += 1
            elif result == 'right':
                win_TK += 1

if win_MS == 0 and win_TK > 0:
    print('TK')
elif win_MS > 0 and win_TK == 0:
    print('MS')
else:
    print('?')
