# 다른 사람 풀이 참고
# https://youtu.be/yYc2KiCSIoA

from itertools import permutations
import math

def solution(n, weak, dist):
    weak_size = len(weak)
    weak = weak + [w + n for w in weak]
    min_friend_cnt = math.inf
    
    for start_idx in range(weak_size): # 각 취약점부터 시작
        for friends in permutations(dist, len(dist)):
            friend_cnt = 1
            position = start_idx
            
            for next_idx in range(1, weak_size):
                next_position = start_idx + next_idx
                weak_dist = weak[next_position] - weak[position] # 현재 취약점과 다음 취약점 사이의 거리
                
                if weak_dist > friends[friend_cnt-1]: # 취약점 사이의 거리가 현재 친구가 갈 수 있는 거리보다 큰 경우 (현재 친구는 다음 취약점까지 커버할 수 없음)
                    position = next_position
                    friend_cnt += 1
                    if friend_cnt > len(dist): # 사용할 수 있는 친구를 모두 사용했지만 모든 취약점을 점검하지 못한 경우
                        break
            
            if friend_cnt <= len(dist): # 모든 취약점을 방문했고, 가능한 범위 내의 친구수를 사용한 경우
                min_friend_cnt = min(min_friend_cnt, friend_cnt)
                
    return min_friend_cnt if min_friend_cnt != math.inf else -1