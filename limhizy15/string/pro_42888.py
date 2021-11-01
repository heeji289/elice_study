# ㅋㅏ카오 2019 오픈채팅방

def solution(record):
    lists = []
    answer = []
    
    names = {}
    
    for r in record:
        message = r.split(' ')
        # 닉네임이 있는 경우
        if len(message) == 3:
            nick = message[2]
        else:
            nick = ''
        sign = message[0]
        uid = message[1]
        
        # uid-닉네임 저장
        if nick != '':
            names[uid] = nick
        
        # sign별로 저장
        if sign == 'Change':
            names[uid] = nick
        else:
            lists.append([sign, uid])
        
    for sign, uid in lists:
        nick = names[uid]
        if sign == 'Enter':
            answer.append(f'{nick}님이 들어왔습니다.')
        elif sign == 'Leave':
            answer.append(f'{nick}님이 나갔습니다.')
    
    return answer