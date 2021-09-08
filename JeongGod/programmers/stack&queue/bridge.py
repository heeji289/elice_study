from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    # bridge_length만큼 견딘다.
    # weight만큼 무게를 견딘다.
    
    bridge = deque([])
    cur_weight = 0
    i = 0
    while i < len(truck_weights):
        answer += 1
        
        if len(bridge) > 0 and bridge[0][0] == answer:
            _, out_truck = bridge.popleft()
            cur_weight -= out_truck
            
            
        if cur_weight+truck_weights[i] <= weight and len(bridge) != bridge_length:
            bridge.append((answer+bridge_length, truck_weights[i]))
            cur_weight += truck_weights[i]
            # 다음 트럭
            i += 1
    return answer+bridge_length
