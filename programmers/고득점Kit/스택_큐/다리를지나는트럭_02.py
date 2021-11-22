# 성공
# 다른 사람 풀이 개선

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    #print(time, bridge, truck_weights)
    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            new_weight = 0 if sum(bridge) + truck_weights[0] > weight else truck_weights.pop(0)
            bridge.append(new_weight)
        #print(time, bridge, truck_weights)
    return time