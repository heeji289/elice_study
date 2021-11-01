from collections import defaultdict

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

'''
풀이 2
- 명령어에 따라 문자열의 구조가 다름
- 가변인자를 받는 함수로 시도(큰 의미는 없을 듯...)
'''


def solution(record):
    answer = []
    users = defaultdict()
    behaviors ={
        'Enter' : '님이 들어왔습니다.',
        'Leave' : '님이 나갔습니다.'
    }

    def set_nickname(behavior, uid, *nickname):
        if nickname:
            users[uid] = nickname[0]

    def message(behavior, uid, *nickname):
        try:
            return users[uid] + behaviors[behavior]
        except:
            return
        
    for rec in record:
        set_nickname(*rec.split(' '))
    
    for rec in record:
        msg = message(*rec.split(' '))
        if msg != None:
            answer.append(msg)

    return answer


'''
풀이 1
- 명령어에 따라 문자열의 구조가 다름
- Enter + uid + nickname
- Change + uid + nickname
- Leave + uid
- if 처리하여 해결
'''

'''
def solution(record):
    answer = []
    users = defaultdict()
    behaviors ={
        'Enter' : '님이 들어왔습니다.',
        'Leave' : '님이 나갔습니다.'
    }

    for rec in record:
        if rec.startswith('C') or rec.startswith('E') :
            behavior, uid, nickname = rec.split(' ')
            users[uid] = nickname
    
    for rec in record:
        if rec.startswith('E'):
            behavior, uid, _ = rec.split(' ')
            answer.append(users[uid]+behaviors[behavior])
        if rec.startswith('L'):
            behavior, uid = rec.split(' ')
            answer.append(users[uid]+behaviors[behavior])

    return answer

'''
