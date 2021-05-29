# 성공

from copy import deepcopy

def get_one_cnt(n):
    return len([i for i in n if i == '1'])

def solution(n):
    nn = deepcopy(n)
    while True:
        nn += 1
        if get_one_cnt(bin(nn)[2:]) == get_one_cnt(bin(n)[2:]): return nn