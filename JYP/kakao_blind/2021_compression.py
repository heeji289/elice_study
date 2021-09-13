from collections import defaultdict
import string

#msg = "KAKAO" # [11, 1, 27, 15]
#msg = "TOBEORNOTTOBEORTOBEORNOT" # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
#msg = "ABABABABABABABAB" # [1, 2, 27, 29, 28, 31, 30]  


def solution(msg):
    
    #1. initizlize table
    table = defaultdict(list)
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
            print(w)
            answer.append(table[w])
            num += 1
            table[c] = num
            start = end
            if end == len(msg):
                print(table[msg[end-1]])
                answer.append(table[msg[end-1]])
                break

        elif c in table:
            if end == len(msg):
                print(table[c])
                answer.append(table[c])
                break

    return answer


#print(solution(msg))