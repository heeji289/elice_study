#s = "aabbaccc"	# 2a2ba3c
#s = "ababcdcdababcdcd"	#2ab2cd2ab2cd 2ababcdcd
#s = "abcabcdede"	
#s = "abcabcabcabcdededededede"	
#s = "xababcdcdababcdcd"
#s = "ababcdcdabab" # 2ab2cd2ab # error case

from collections import defaultdict

def solution(s):

    result = []

    for i in range(1, len(s)+1): # step size
        answer = ""
        table = defaultdict(int)
        j = 0
        cnt = 1
        while j < len(s):    
            curr = str(s[j:j+i] if j+i <= len(s) else "")
            next = str(s[j+i:j+i+i] if j+i+i <= len(s) else "")
            
            if curr == next:
                cnt += 1
            elif curr != next:
                if next != "":
                    if cnt != 1:
                        answer += str(cnt)+curr
                        cnt = 1
                    elif cnt == 1:
                        answer += curr
                elif next == "":
                    if cnt != 1:
                        answer += str(cnt)+s[j:]
                    elif cnt == 1:
                        answer += s[j:]

            j += i
        result.append(len(answer))
        #debug   
        # print('i', i, 'answer',answer, "table", table)
    
    return min(result)


#print(solution(s))