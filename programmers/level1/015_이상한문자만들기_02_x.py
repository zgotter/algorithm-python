# 다른 사람 풀이 ()
# https://velog.io/@joygoround/test-%EC%9D%B4%EC%83%81%ED%95%9C-%EB%AC%B8%EC%9E%90-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# - 이것도 실패

def solution(s):
    words_list = s.split()
    new_list = []
    for word in words_list:
        new_words = ''
        for i in range(len(word)):
            new_words += word[i].upper() if i%2 == 0 else word[i].lower()
        new_list.append(new_words)
    return ' '.join(new_list)

print(solution("try hello world"))