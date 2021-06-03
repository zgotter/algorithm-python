# 3번째 테스트 케이스 실패

def solution(m, musicinfos):
    ans = []
    musics = {}
    for mu in musicinfos:
        st, et, title, melody = mu.split(',')
        du = (int(et.split(':')[0]) - int(st.split(':')[0]))*60 + (int(et.split(':')[1]) - int(st.split(':')[1]))
        melody = melody * (du//len(melody)+1)
        dic = {'st': st, 'et': et, 'du': du, 'me': melody[:du]}
        musics[title] = dic
        
    for k in musics.keys():
        me = musics[k]['me']
        if len(me) == len(m):
            if m == me:
                ans.append(k)
        else:
            for i in range(0, len(me)-len(m)):
                if m == me[i:len(m)+i]:
                    ans.append(k)
                    break
    if len(ans) == 0:
        return '(None)'
    elif len(ans) == 1:
        return ans[0]
    else:
        lst = [(k, musics[k]['du']) for k in ans]
        lst.sort(key=lambda x: x[1], reverse=True)
        print(lst)
        return lst[0][0]