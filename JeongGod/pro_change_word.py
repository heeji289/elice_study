from collections import deque
def solution(begin, target, words):
    visited = [0 for i in range(len(words))]
    val = 0
    dq = deque()
    if target in words:
        dq.append((begin, val))
    ab = False

    while dq:
        # 단어를 뽑는다.
        result, val = dq.popleft()

        if result == target:
            return val
        
        # result를 쪼갠다.
        coms = []
        for i in range(len(result)):
            coms.append((result[:i], result[i+1:]))
        # 덱에 넣을지 말지 판단
        com = ""
        for idx, word in enumerate(words):
            # 방문한적이 있다면 스킵
            if visited[idx] == 1:
                continue
            flag = True
            for com in coms:
                if word.startswith(com[0]) and word.endswith(com[1]):
                    dq.append((word, val+1))
                    visited[idx] = 1
    return 0