# 다른 사람 풀이 참고
# https://velog.io/@tjdud0123/%EC%99%B8%EB%B2%BD-%EC%A0%90%EA%B2%80-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    candidates = []
    expanded_weak = weak + [w + n for w in weak]
    
    for i, start in enumerate(weak):
        for friends in permutations(dist):
            friend_cnt = 1
            position = start
            
            for friend in friends:
                position += friend
                if position < expanded_weak[i + weak_len - 1]: # 끝 포인트까지 도달 못 했을 때
                    friend_cnt += 1 # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    for w in expanded_weak[i+1:i+weak_len]:
                        if w > position:
                            position = w
                            break
                else: # 끝 포인트까지 도달
                    candidates.append(friend_cnt)
                    break

    answer = min(candidates) if candidates else -1
    return answer