from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    i = 0
    current_weight = 0
    while i < len(truck_weights):
        current_weight -= bridge.popleft()
        if current_weight + truck_weights[i] <= weight:
            current_weight += truck_weights[i]
            bridge.append(truck_weights[i])
            i+=1
        else:
            bridge.append(0)
        answer+=1
    while bridge:
        bridge.popleft()
        answer+=1
    
    return answer