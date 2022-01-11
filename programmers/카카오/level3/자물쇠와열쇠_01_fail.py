# 일부 테스트 케이스 실패 (23, 25, 33)

from copy import deepcopy

m, n, mm, nn = 0, 0, 0, 0

def get_expanded_lock(lock):
    global m, n, mm, nn
    expanded_lock = [[0 for _ in range(nn)] for _ in range(nn)]
    for i in range(nn):
        for j in range(nn):
            if mm <= i < n+mm and mm <= j < n+mm:
                if lock[i-mm][j-mm] == 1:
                    expanded_lock[i][j] = 1
    return expanded_lock

def get_expanded_key(key, x, y):
    global m, n, mm, nn
    expanded_key = [[0 for _ in range(nn)] for _ in range(nn)]
    for i in range(nn):
        for j in range(nn):
            if x <= i < x+m and y <= j < y+m:
                expanded_key[i][j] = key[i-x][j-y]
    return expanded_key

def merge(key, lock):
    global m, n, mm, nn
    merged = [[0 for _ in range(nn)] for _ in range(nn)]
    for i in range(nn):
        for j in range(nn):
            merged[i][j] = 1 if key[i][j] or lock[i][j] else 0
    return merged

def check(merged):
    global m, n, mm, nn
    for i in range(mm, n+mm):
        for j in range(mm, n+mm):
            if not merged[i][j]:
                return False
    return True

def rotate(key):
    global m, n, mm, nn
    new_key = deepcopy(key)
    for i in range(m):
        for j in range(m):
            new_key[j][m-i-1] = key[i][j]
    return new_key
    
def solution(key, lock):
    global m, n, mm, nn
    m, n = len(key), len(lock)
    mm = m-1
    nn = n+mm*2
    expanded_lock = get_expanded_lock(lock)
    rotated_key = deepcopy(key)
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for i in range(nn-mm):
            for j in range(nn-mm):
                expanded_key = get_expanded_key(rotated_key, i, j)
                merged = merge(expanded_key, expanded_lock)
                if check(merged):
                    return True
    return False