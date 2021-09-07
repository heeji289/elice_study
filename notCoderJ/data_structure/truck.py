'''
  풀이요약
    1. 다리 길이만큼 0으로 채워진 다리와 트럭 대기열을 정의합니다.
    2. 트럭 대기열이 끝날 때까지 다리의 맨 앞쪽부터 값을 하나씩 제거하면서 현재 다리 위의 총 무게(total)를 계산하고 시간(answer)을 1 증가시킵니다.
    3. 현재 다리 위의 무게에 다음 트럭을 추가했을 때 최대 무게이하라면 해당 트럭을 다리에 추가해줍니다.
    4. 다리의 최대 무게를 넘었다면 다리에 0을 추가하여 다음 트럭을 대기시킵니다.
    5. 트럭 대기열이 끝난 후에도 다리 위에 트럭이 남아있는 경우를 위해 현재 누적 시간(answer)에 남은 다리의 길이만큼 더해줍니다.
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    total = 0
    while trucks:
        answer += 1
        total -= bridge.popleft()
        if total + trucks[0] <= weight:
            current = trucks.popleft()
            total += current
            bridge.append(current)
        else:
            bridge.append(0)
            
    return answer + len(bridge)
    

# def solution(bridge_length, weight, truck_weights):
#     answer = bridge_length
#     dq = deque(truck_weights)
#     on_bridge = deque([])
    
#     total = 0
#     while dq:
#         current = dq.popleft()
#         if total + current <= weight and len(on_bridge) < bridge_length:
#             answer += 1
#             total += current
#             on_bridge.append([current, answer])
#             continue
        
#         while total + current > weight or len(on_bridge) >= bridge_length:
#             pass_truck, answer = on_bridge.popleft()
#             total -= pass_truck
#         answer += bridge_length
#         total += current
#         on_bridge.append([current, answer])
# 
    # return answer