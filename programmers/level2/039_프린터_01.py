# 성공

def solution(priorities, location):
    answer = 0
    lst = [(i, p) for i, p in enumerate(priorities)]
    res = []
    while True:
        doc = lst.pop(0)
        if len(lst) == 0:
            res.append(doc)
            break
        if doc[1] >= max([l[1] for l in lst]):
            res.append(doc)
        else:
            lst.append(doc)
    for i in range(len(res)):
        if res[i][0] == location:
            return i+1
