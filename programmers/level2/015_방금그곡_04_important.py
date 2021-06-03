# 성공
# 다른 사람 풀이

def trans(m):
    return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    m = trans(m)
    ans = ''
    result = None
    dic = dict()
    for info in musicinfos:
        start, end, title, sound = info.split(',')
        h1, m1 = start.split(':')
        h2, m2 = end.split(':')
        time = (int(h2) - int(h1))*60 + int(m2) - int(m1)
        sound = trans(sound)
        sound = sound*(time//len(sound)) + sound[0:time%len(sound)]
        dic[sound] = title
    for song in dic.keys():
        if m in song:
            if result == None:
                result = song
            else:
                if len(result) < len(song):
                    result = song
    return dic[result] if result != None else '(None)'
    