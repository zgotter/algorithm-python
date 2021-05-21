# 다른 사람 풀이 참조 코드 개선
# 성공
# 10진수 -> 2진수 변환 : bin()

def solution(n, arr1, arr2):
    
    arr1 = [list(bin(a)[2:].zfill(n).replace('0',' ').replace('1','#')) for a in arr1]
    arr2 = [list(bin(a)[2:].zfill(n).replace('0',' ').replace('1','#')) for a in arr2]
    
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '#':
                arr2[i][j] = '#'
    
    return [''.join(a) for a in arr2]
