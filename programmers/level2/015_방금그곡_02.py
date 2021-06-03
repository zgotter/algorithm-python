# 테스트 8번 하나만 실패... ㅠㅠ

def get_du(st, et):
    return (int(et.split(':')[0]) - int(st.split(':')[0]))*60 + (int(et.split(':')[1]) - int(st.split(':')[1]))

def get_me(melody, du):
    me = []
    for i in range(len(melody)):
        if i < len(melody)-1:
            if melody[i] == '#': continue
            else:
                if melody[i+1] == '#':
                    me.append(melody[i:i+2])
                else:
                    me.append(melody[i])
        else:
            if melody[i] != '#': me.append(melody[i])
    if du == 0:
        return me
    else:
        res = []
        for i in range(du):
            res.append(me[i%len(me)])
        return res
                
def solution(m, musicinfos):
    ans = []
    musics = {}
    
    for mu in musicinfos:
        st, et, title, melody = mu.split(',')
        musics[title] = {'du': get_du(st, et), 'me': get_me(melody, get_du(st, et))}

    mm = get_me(m, 0)
    
    for k in musics.keys():
        me = musics[k]['me']
        if len(me) == len(mm):
            if me == mm:
                ans.append((k, musics[k]['du']))
        else:
            for i in range(len(me)-len(mm)):
                if mm == me[i:len(mm)+i]:
                    ans.append((k, musics[k]['du']))
                    break
    
    ans.sort(key=lambda x: x[1], reverse=True)
    
    return ans[0][0] if len(ans) > 0 else '(None)'