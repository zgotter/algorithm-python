# 정확성 테스트 모두 성공
# 효율성 테스트 케이스 2개(3,4) 실패 (시간 초과)

def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            l = len(phone_book[i])
            if phone_book[i] == phone_book[j][:l]:
                return False
    return True