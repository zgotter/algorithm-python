# 성공
# 다른 사람 풀이

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c: return p
    return participant.pop()