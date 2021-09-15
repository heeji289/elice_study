def solution(citations):
    citations.sort()
    
    if citations[0] > len(citations):
        return len(citations)
    if citations[-1] < len(citations):
        return citations[-1]
    
    for i in range(len(citations)-1, -1, -1):
        if citations[i] == len(citations[i:]):
            return citations[i]
        elif citations[i] < len(citations[i:]):
            for j in range(citations[i+1], citations[i]-1, -1):
                if j == len(citations[i+1:]):
                    return j
        else: #citations[i] > len(citations[i:]):
             for j in range(citations[i], citations[i]-1, -1):
                if j == len(citations[i:]):
                    return j