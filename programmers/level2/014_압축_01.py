# 성공

def solution(msg):
    ans = []
    dic = {chr(i+65):i+1 for i in range(26)}
    while len(msg) > 0:
        idx = len(msg)
        while True:
            w = msg[:idx]
            if w in dic.keys():
                print(w)
                ans.append(dic[w])
                dic[msg[:idx+1]] = max(dic.values())+1
                msg = msg[len(w):]
                break
            else:
                idx -= 1
    return ans

print(solution('KAKAO'))