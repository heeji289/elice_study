'''
    풀이 요약:
        먼저, 처음 주어진 단어들에 target이 없는 경우 변경이 불가능하므로 0을 바로 리턴해주고
        그외의 경우 dfs를 반복적으로 수행하여 시작 단어와 1글자만 다른 단어들로 계속 변경하며 target문자에 도달할 수 있는 경우
        현재 answer와 현재까지 변경한 수(전체 단어 수 - 현재 남은 단어 수)를 비교한 후 작은 값으로 answer를 변경하는 과정을 반복헀습니다.
        만약 dfs가 종료된 후에도 answer값이 초기 설정한 무한 값이면 변경할 수 없기 때문에 0을 반환했습니다.
'''

# 새로 짠 코드
def check(x, y):
    if not x:
        return 0
    cnt = 1 if x[0] != y[0] else 0
    return cnt + check(x[1:], y[1:])

def solution(begin, target, words):
    if target not in words:
        return 0
    
    print(begin, target, words)
    answer = int(1e9)
    total = len(words)
    
    def dfs(begin, target, words):
        nonlocal answer
        if begin == target:
            answer = min(answer, total - len(words))
        
        for i, word in enumerate(words):
            if check(begin, word) == 1:
                dfs(word, target, words[:i] + words[i + 1:])
    
    dfs(begin, target, words)
    
    return answer if answer != int(1e9) else 0


# 이전에 짰던 코드
def dfs(begin, target, words):
    if begin == target:
        return len(words)
    
    remain = -1
    for i in range(len(words)):
        if [i != j for i, j in zip(begin, words[i])].count(True) == 1:
            remain = max(remain, dfs(words[i], target, words[:i] + words[i+1:]))
        
    return remain

def solution(begin, target, words):
    answer = 0
    if target in words:
        remain = dfs(begin, target, words)
        answer = len(words) - remain if remain > -1 else 0
    
    return answer
