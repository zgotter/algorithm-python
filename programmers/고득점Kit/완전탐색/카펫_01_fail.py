# 일부 테스트케이스 실패 (4, 6, 7)

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    width_list = [i+1 for i in range(total//2) if total % (i+1) == 0] + [total]
    width_list.sort(reverse=True)
    
    square = [(w, total//w) for w in width_list if w >= (total//w)]
    answer = [s for s in square[-1]]
    
    return answer