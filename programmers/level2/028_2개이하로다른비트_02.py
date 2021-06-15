# 성공
# 다른 사람 풀이 참고

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            bin_num = list(bin(number)[2:])
            bin_num[-1] = '1'
        else:
            bin_num = '0' + bin(number)[2:]
            idx = bin_num.rfind('0')
            bin_num = list(bin_num)
            bin_num[idx] = '1'
            bin_num[idx+1] = '0'
        ans_num = int(''.join(bin_num), 2)
        answer.append(ans_num)
    return answer