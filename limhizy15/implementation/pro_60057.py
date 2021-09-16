# [2020 kakao] 문자열 압축

def solution(s):
    answer = len(s)
    
    # 문자열 절반 이상으로 자를 수 없으므로 범위지정은 아래와 같이 함
    for size in range(1, len(s) // 2 + 1):
        before = s[0:size]
        target = ''
        cnt = 1 

        # size만큼 탐색
        for i in range(size, len(s), size):
            str_ = s[i:i+size]
            
            # 이전 문자열과 같으면
            if before == str_:
                cnt += 1
            else:
                target += str(cnt) if cnt > 1 else ''
                target += before

                # 변수들 변경
                cnt = 1 
                before = str_

        # 남는 부분 예외처리    
        target += str(cnt) if cnt > 1 else ''
        target += before
        cnt = 1 
        before = str_
        
        if len(target) < answer:
            answer = len(target)
            
    return answer