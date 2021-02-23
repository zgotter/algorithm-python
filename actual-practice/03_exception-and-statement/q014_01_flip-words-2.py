# 문제명 : 단어 뒤집기 2
# url : https://www.acmicpc.net/problem/17413

# 직접 풀이 (1) - 성공

S = input()
lst = []

while len(S) != 0:
    if S[0] == '<':
        idx = S.find('>')
        lst.append(S[:idx+1])
        S = S[idx+1:]
    else:
        idx = S.find('<')
        if idx == -1:
            lst.extend(S.split())
            S = ''
        else:
            lst.extend(S[:idx].split())
            S = S[idx:]

result = ''
for i in range(len(lst)):
    if lst[i].find('<') > -1:
        result += lst[i]
    else:
        result += lst[i][::-1]
    if (i < len(lst)-1) and (lst[i].find('<') == -1) and (lst[i+1].find('<') == -1):
        result += ' '

print(result)
