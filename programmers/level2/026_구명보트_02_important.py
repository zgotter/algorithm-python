# 성공
# 다른 사람 풀이 참고

def solution(people, limit):
    answer = 0
    people.sort()
    si, ei = 0, len(people)-1
    while si <= ei:
        answer += 1
        if people[si]+people[ei] <= limit:
            si += 1
        ei -= 1
    return answer