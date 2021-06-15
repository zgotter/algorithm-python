# 실패 (효율성 테스트 시간초과)

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while True:
        if len(people) == 1:
            answer += 1
            people.pop()
            break
        if len(people) == 0:
            break
        weight = people[0] + people[-1]
        if weight <= limit:
            people.pop()
        people.pop(0)
        answer += 1
    return answer