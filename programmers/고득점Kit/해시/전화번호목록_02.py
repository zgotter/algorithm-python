# 효율성 테스트 3,4번 실패

def solution(phone_book):
    for i in range(len(phone_book)):
        phone = phone_book[i]
        sub_list = [p for j, p in enumerate(phone_book) if i != j]
        check = [p.startswith(phone) for p in sub_list]
        if sum(check) > 0:
            return False
    return True