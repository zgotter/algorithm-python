# 성공
# 다른 사람 풀이
# collections.Counter()
#  - 리스트의 각 원소와 갯수를 딕셔너리 형태로 리턴
#  - 마이너스 연산 가능

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))