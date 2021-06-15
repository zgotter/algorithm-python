# 성공

def solution(n, words):
    answer = [0,0]
    people = [0 for _ in range(n+1)]
    olds = []
    prev = ''
    for idx, word in enumerate(words):
        pos = (idx%n)+1
        if prev == '':
            prev = word
            people[pos] += 1
            olds.append(word)
        else:
            if word not in olds:
                if prev[-1] == word[0]:
                    prev = word
                    people[pos] += 1
                    olds.append(word)
                else:
                    answer[0] = pos
                    answer[1] = people[pos]+1
                    break
            else:
                answer[0] = pos
                answer[1] = people[pos]+1
                break
    return answer