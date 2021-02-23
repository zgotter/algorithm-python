# 문제명 : 단어 뒤집기 2
# url : https://www.acmicpc.net/problem/17413

# 해설 (2) - 성공
#  - 결과 변수(ans) 사용

S, tmp = input(), ''
ck = False
ans = ''

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + ' '
            tmp = ''
        else:
            ans += ' '
    elif i == '<':
        ck = True
        ans += tmp[::-1] + '<'
        tmp = ''
    elif i == '>':
        ck = False
        ans += '>'
    else: # 알파벳, 숫자
        if ck:
            ans += i
        else:
            tmp += i

ans += tmp[::-1] + ' '

print(ans)