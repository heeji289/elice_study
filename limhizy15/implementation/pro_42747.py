# [정렬] H-Index

def solution(citations):
    answer = 0
    
    # answer = sum(citations) // len(citations)
    citations.sort()
    size = len(citations)
    
    for i in range(size):
        cnt = size - i
        if citations[i] >= cnt:
            answer = cnt
            break
    
    return answer