# 정확성 테스트 케이스 2개(11, 14) 실패
# 효율성 테스트 모두 성공

def solution(phone_book):
    min_len = min([len(phone) for phone in phone_book])
    lst = [phone[:min_len] for phone in phone_book]
    lst2 = list(set(lst))
    return len(lst) == len(lst2)