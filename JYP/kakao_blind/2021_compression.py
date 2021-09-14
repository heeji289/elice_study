from collections import defaultdict
import string

#msg = "KAKAO" # [11, 1, 27, 15]
#msg = "TOBEORNOTTOBEORTOBEORNOT" # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
#msg = "ABABABABABABABAB" # [1, 2, 27, 29, 28, 31, 30]  


def solution(msg):
    
    #1. initizlize table
    table = defaultdict(int)
    for idx, alphabet in enumerate(string.ascii_uppercase):
        table[alphabet] = idx+1

    #2. LZW implementation
    answer = []
    num = 26
    start = 0
    end = 0
    while start < len(msg):
        end += 1
        w = msg[start:end]
        c = msg[start:end+1]
        if c not in table:
            answer.append(table[w])
            num += 1
            table[c] = num
            start = end
            continue

        elif c in table:
            if end == len(msg):
                answer.append(table[c])
                break

    return answer


#print(solution(msg))