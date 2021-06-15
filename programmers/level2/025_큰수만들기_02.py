# 샘플 실패

def solution(number, k):
    answer = []
    num_lst = [int(n) for n in number]
    while len(answer) < (len(number)-k):
        print(num_lst)
        v = 0
        idx = 0
        for i, n in enumerate(num_lst):
            idx = i
            if v <= n:
                v = n
            else:
                break
        answer.append(v)
        num_lst.pop(idx-1)
    return ''.join(map(str, answer))