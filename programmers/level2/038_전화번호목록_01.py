# 정확성 테스트 케이스 2개(15, 19) 실패
# 효율성 테스트 케이스 2개(3,4) 실패 (시간 초과)

def solution(phone_book):
    answer = True
    min_len = min([len(phone) for phone in phone_book])
    pre_phone = [phone for phone in phone_book if len(phone) == min_len]
    for pre in pre_phone:
        for phone in phone_book:
            if pre == phone:
                continue
            if pre == phone[:min_len]:
                return False
    return answer