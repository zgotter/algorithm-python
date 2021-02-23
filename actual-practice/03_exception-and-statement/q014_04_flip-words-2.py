# 문제명 : 단어 뒤집기 2
# url : https://www.acmicpc.net/problem/17413

# 해설 (3) - 성공
#  - 코드 정리

S = input()
ck, tmp, ans = False, '', ''

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + ' '
            tmp = ''
        else: ans += ' '
    elif i == '<':
        ck = True
        ans += tmp[::-1] + '<'
        tmp = ''
    elif i == '>':
        ck = False
        ans += '>'
    else: # 알파벳, 숫자
        if ck: ans += i
        else: tmp += i

ans += tmp[::-1] + ' '

print(ans)