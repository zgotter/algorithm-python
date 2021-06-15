# 실패 (테스트 케이스 10, 11, 시간초과)

def set_len(b, l):
    return b.rjust(l, '0')

def get_diff_bit_cnt(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]: cnt += 1
    return cnt

def solution(numbers):
    answer = []
    for number in numbers:
        bit1 = bin(number)[2:]
        max_len = len(bit1)+1
        bit1 = set_len(bit1, max_len)
        
        num = number+1
        res = ''
        while True:
            bit2 = bin(num)[2:]
            bit2 = set_len(bit2, max_len)
            if get_diff_bit_cnt(bit1, bit2) in [1,2]:
                res = num
                break
            num += 1
        answer.append(res)

    return answer