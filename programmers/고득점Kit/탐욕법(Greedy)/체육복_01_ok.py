# 성공

def solution(n, lost, reserve):
    student = [0 if (i+1) in lost else 1 for i in range(n)]
    student = [s+1 if i+1 in reserve else s for i, s in enumerate(student)]
    for i, s in enumerate(student):
        if s == 0:
            if i > 0 and student[i-1] == 2:
                student[i-1] -= 1
                student[i] = 1
            elif i < n-1 and student[i+1] == 2:
                student[i+1] -= 1
                student[i] = 1
    return len([s for s in student if s > 0])