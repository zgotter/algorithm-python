# 일부 테스트 케이스 실패 (런타임 에러)

def solution(n, lost, reserve):
    stu = [0 if i in lost else 1 for i in range(n+1)]
    for i in range(1, len(stu)):
        if stu[i] != 0: continue
        print(i)
        if i-1 in reserve:
            stu[i] = 1
            reserve.remove(i-1)
            continue
        if i+1 in lost:
            stu[i] = 1
            reserve.remove(i+1)
            
    answer = [s for s in stu if s == 1]
        
    return len(answer)-1