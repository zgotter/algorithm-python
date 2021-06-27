# 정확성 테스트 모두 성공
# 효율성 테스트 케이스 2개(3,4) 실패 (시간 초과)

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for i in range(len(phoneBook)-1):
        for j in (i+1, len(phoneBook)):
            if phoneBook[j].startswith(phoneBook[i]):
                return False
    return True