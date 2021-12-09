# 테스트 5번만 실패

def solution(s):
    answer = 1000
    n = len(s)
    for i in range(1, n//2+1):
        lst = [s[j:j+i] for j in range(0, n, i)]
        used = [False for _ in range(len(lst))]
        res = ""
        for j in range(len(lst)):
            if used[j]:
                continue
            used[j] = True
            cnt = 1
            for k in range(j+1, len(lst)):
                if not used[k] and lst[j] == lst[k]:
                    cnt += 1
                    used[k] = True
                else:
                    break
            res = res + (str(cnt) if cnt > 1 else "") + lst[j]
        answer = min(answer, len(res))
    return answer