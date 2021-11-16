# 효율성 테스트 3,4번 실패

def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    cnt = len(phone_book)
    for i in range(cnt-1):
        for j in range(i+1, cnt):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True