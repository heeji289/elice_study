def solution(s):
    answer = len(s)
    # n개 만큼 자른다.
    for n in range(1, len(s)-1):
        same = 1
        tmp = len(s)
        for i in range(0, len(s), n):
            # 같은 것이 있다면
            if s[i:i+n] == s[i+n:i+(2*n)]:
                # 길이를 빼준다.
                tmp -= n
                same += 1
                continue
            # 다르다면 같은 것이 존재했는지 판단
            if same != 1:
                tmp += len(str(same))
                same = 1
        
        answer = min(answer, tmp)
                
    return answer
