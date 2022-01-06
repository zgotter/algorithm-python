# 일부 테스트케이스 실패 (런타임 에러)

import re

def get_play_time(s_time, e_time):
    s_h, s_m = map(int, s_time.split(":"))
    e_h, e_m = map(int, e_time.split(":"))
    if s_h == e_h:
        return e_m - s_m
    else:
        return 60 - s_m + e_m

def split_score(score):
    score_list = []
    while True:
        if len(score) == 1:
            score_list.append(score)
            break
        elif len(score) == 2 and score[-1] == "#":
            score_list.append(score)
            break
        if score[1] == "#":
            score_list.append(score[:2])
            score = score[2:]
        else:
            score_list.append(score[0])
            score = score[1:]
    return score_list
        
    
def solution(m, musicinfos):
    answer = []
    sound = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    for musicinfo in musicinfos: # score: 악보
        s_time, e_time, title, score = musicinfo.split(",")
        
        play_time = get_play_time(s_time, e_time)

        score = split_score(score)
        full_score = score * ((play_time // len(score)) + 1)
        full_score = full_score[:play_time]
        
        music = split_score(m)
        music_len = len(music)
        
        is_match = False
        for i in range(0, len(full_score)-len(music)):
            if full_score[i:i+music_len] == music:
                is_match = True
                break
        
        if is_match:
            answer.append((title, play_time))
        
    answer = sorted(answer, key=lambda x: -x[1])
    
    return answer[0][0]