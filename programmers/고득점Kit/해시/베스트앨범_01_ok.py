# 성공

def solution(genres, plays):
    answer = []
    g_unique = list(set(genres))
    g_plays = {g: 0 for g in g_unique}
    g_songs = {g: [] for g in g_unique}
    for i, (g, p) in enumerate(zip(genres, plays)):
        g_plays[g] += p
        g_songs[g].append((p, i))
    g_plays = [(g, p) for g, p in g_plays.items()]
    g_plays = sorted(g_plays, key=lambda x: -x[1])
    for g, _ in g_plays:
        songs = g_songs[g]
        songs = sorted(songs, key=lambda x: (-x[0], x[1]))
        if len(songs) > 1:
            songs = songs[:2]
        song_idx = [i for _, i in songs]
        answer.extend(song_idx)
    return answer