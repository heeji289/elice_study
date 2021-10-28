def solution(record):
    """
    id를 key = 닉네임 value
    1. 먼저 [key(id), "~~ 했습니다"] answer에다 넣는다.
    2. 그런 뒤에 key(id)를 value(nickname)로 변경한다.
    3. 그리고 [value(nickname), "~~ 했습니다"]를 join으로 잇는다.
    """
    user = dict()
    answer = []
    for sen in record:
        command, *rest = sen.split()
        if command == "Enter":
            user[rest[0]] = rest[1]
            answer += [[rest[0], "님이 들어왔습니다."]]
        elif command == "Leave":
            answer += [[rest[0], "님이 나갔습니다."]]
        elif command == "Change":
            user[rest[0]] = rest[1]

    for idx in range(len(answer)):
        nickname = user.get(answer[idx][0])
        # "님이 들어왔습니다" 같은건 패스
        if nickname is None:
            continue
        answer[idx][0] = nickname
        answer[idx] = "".join(answer[idx])
    return answer
