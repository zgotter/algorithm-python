# 정확성 테스트 케이스 2개(11, 14) 실패
# 효율성 테스트 모두 성공

def solution(phone_book):
    answer = True
    len_lst = sorted(list(set([len(phone) for phone in phone_book])))
    for i in len_lst:
        if len(phone_book) != len(set([phone[:i] for phone in phone_book])):
            answer = False
            break
    return answer