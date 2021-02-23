# 문제명 : 단어 뒤집기 2
# url : https://www.acmicpc.net/problem/17413

# 해설 (1) - 성공

S, tmp = input(), ''
ck = False
for i in S:
    if i == ' ':
        if not ck:
            print(tmp[::-1], end=' ')
            tmp = ''
        else:
            print(' ', end='')
    elif i == '<':
        ck = True
        print(tmp[::-1] + '<', end='')
        tmp = ''
    elif i == '>':
        ck = False
        print('>', end='')
    else: # 알파벳, 숫자
        if ck:
            print(i, end='')
        else:
            tmp += i

print(tmp[::-1], end=' ')