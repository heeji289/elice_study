# 단어 변환

"""
[문제]
begin에서 target까지 가장 짧은 변환 단계를 구해라
변환시 단어는 1글자만 바꿀 수 있고 그 단어가 words안에 있어야 한다.
모든 단어의 길이는 같다. (3이상 10이하)

[틀린 풀이]
visited = [words만큼]
1. begin부터 시작해서 words를 탐색한다.
- 재귀를 이용한 DFS탐색
2. words 안에서 아직 방문하지 않았고, 단어 1개만 바꿀 수 있으면 방문한다.
=> 예외처리를 신경쓰지 못했고, 깊이(answer)을 갱신해주는 위치가 잘못되었다.

[맞은 풀이]
1. target이 words 배열에 없으면 0을 리턴 (예외처리)
2. stack을 이용한 DFS 탐색
    1) 시작점을 스택에 넣고 스택이 빌 때까지 
    2) 만약 스택 pop한 값이 target이면 정답이므로 리턴
    3) 아닌 경우, words를 순회하면서 현재 단어와 한 글자만 다른지 체크
    4) 해당 글자를 아직 방문 안햇으면 방문해주고 스택에 넣어준다.
    5) words 탐색이 끝나면 answer + 1 
    ******** 원래 4)에서 answer + 1을 해주어서 틀렸다.

*** 전역변수를 함수 안에서 참조할 때 global.. 주의해서 쓸 것
*** 참고 : https://khann.tistory.com/79
"""

answer = 0

# count_diff(a, b) : 두 글자의 단어 차이 수가 1인지 확인
def count_diff(a, b):
    cnt = 0
    # for문 두 개로..
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    
    if cnt == 1:
        return True
    else:
        return False

# DFS
def dfs(begin, target, visited, words):
    global answer
    s = [begin]

    while s:
        cur = s.pop()
    
        # 종료조건 : 만약 현재 단어가 target과 같은 경우
        if cur == target:
            return answer
    
        # words 안에서 
        for idx in range(len(words)):
            # 단어가 1개 차이나는 것 중에
            if count_diff(words[idx], cur):
                # 이미 방문하지 않은 것을 스택에 넣는다.
                if visited[idx]: continue
                visited[idx] = True
                s.append(words[idx])
        
        answer += 1


def solution(begin, target, words):
    
    global answer

    # target이 words 안에 없을 경우 예외처리
    if target not in words:
        return 0
    
    # words 배열 방문 체크
    visited = [False for i in words]

    dfs(begin, target, visited, words)
    
    return answer


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))
