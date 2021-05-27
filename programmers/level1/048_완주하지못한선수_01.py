# 효율성 테스트 실패

def solution(participant, completion):
    for c in completion:
        participant.pop(participant.index(c))
    return participant[0]