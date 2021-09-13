import string


def solution(msg):
    answer = []
    '''
    1. 첫 문자 + 다음 문자가 dict에 있는지 판단
    1-1 있다면
        1번 반복
    1-2 없다면
        1. answer에 해당 색인문자 append
        2. 주어진 msg에서 지금까지 더한 문자열(마지막 문자는 X) 제거.
        3. 해당 문자열 dict에 추가
    '''
    lzw_dict = {}
    for idx, val in enumerate(string.ascii_uppercase):
        lzw_dict[val] = idx+1
    
    # 색인번호 기억
    rem_num = 26
    while True:
        cur_idx = 0
        w = msg[cur_idx]
        # w인 최장 문자열을 찾는다.
        while w in lzw_dict and cur_idx < len(msg)-1:
            cur_idx += 1
            w += msg[cur_idx]
            
        # w에 해당하는 색인번호 추가
        # 만약, 위 while문에서 마지막 조건으로 인해 탈출했다면
        # 마지막 문자열일테니 탈출
        if w in lzw_dict:
            answer.append(lzw_dict[w])
            break
        answer.append(lzw_dict[w[:-1]])

        # dict에 없는 문자열이면 새로 넣어준다.
        if w not in lzw_dict:
            rem_num += 1
            lzw_dict[w] = rem_num
        
        # msg에서 해당 문자열까지 제거한다.
        msg = msg[cur_idx:]
    
    return answer
