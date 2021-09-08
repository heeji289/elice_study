import heapq
def solution(operations):
    pop_cnt = 0
    max_hq, min_hq = [], []
    
    
    for oper in operations:
        com, num = oper.split()
        num = int(num)
        if com == "I":
            heapq.heappush(max_hq, -num)
            heapq.heappush(min_hq, num)
        elif com == "D":
            # pop한 개수를 센다.
            pop_cnt += 1
            if num == 1:
                # 배열의 모든 것을 다 pop을 한 게 아니라면 가능
                if len(max_hq) - pop_cnt > 0:
                    heapq.heappop(max_hq)
                else:
                    # 배열의 모든 것을 pop했다.
                    pop_cnt = 0
                    max_hq = []
                    min_hq = []
            else:
                if len(min_hq) - pop_cnt > 0:
                    heapq.heappop(min_hq)
                else:
                    pop_cnt = 0
                    max_hq = []
                    min_hq = []
                
    # 개수로 따지자. 
            
    return [-max_hq[0], min_hq[0]] if max_hq and min_hq else [0,0]
