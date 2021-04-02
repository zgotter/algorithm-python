# 소인수분해 함수
#  - https://lsh-story.tistory.com/68

from collections import defaultdict

def get_prime_factor(num):
    dic = defaultdict(int)
    d = 2
    while d <= num:
        if num % d == 0:
            dic[d] += 1
            num = num/d
        else:
            d += 1
    return dic

print(get_prime_factor(6).items())
print(list(get_prime_factor(6).keys()))

def get_prime_factor_list(num):
    dic = defaultdict(int)
    d = 2
    while d <= num:
        if num % d == 0:
            dic[d] += 1
            num = num/d
        else:
            d += 1
    return list(dic.keys())

print(get_prime_factor_list(6))