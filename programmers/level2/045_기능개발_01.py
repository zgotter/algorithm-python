# 성공

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    done = [False for _ in range(n)]
    while sum(done) < n:
        progresses = [min(progresses[i] + speeds[i], 100) for i in range(n)]
        lst = [progresses[i] for i in range(n) if done[i] == False]
        if lst[0] != 100: continue
        cnt = 0
        for i in range(n):
            if done[i] == True: continue
            if progresses[i] == 100:
                done[i] = True
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
    return answer