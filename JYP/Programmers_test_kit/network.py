from collections import deque

'''
풀이3 : 그래프 탐색
- 양방향 네트워크
- 1번 컴퓨터가 2, 3번과 연결되어 있다면
- 2, 3번 컴퓨터와 다른 컴퓨터의 연결 상태를 탐색하고 각각 방문 처리
- 탐색이 종료되면 네트워크 카운트 +1
'''

def solution(n, computers):
    visited = [False]* n 

    def search(x, y):
        q = deque([(x, y)])
        while q:
            x, y = q.popleft() # x, y = q.pop()을 해도 결과는 동일
            visited[y] = True

            for i in range(n):
                if computers[y][i] == 1 and visited[i] == False:
                    q.append((y, i))
                
                # 재방문하지 않을 것이므로 방문한 컴퓨터는 연결을 끊어두기
                computers[y][i] = 0

    answer = 0

    for i in range(n):
        for j in range(n):
            
            # 위에서 연결을 끊어둔 컴퓨터 때문에 네트워크 카운트 시 중복이 일어나지 않음
            if computers[i][j] == 1:
                search(i, j)
                answer += 1

    return answer


'''
TEST CASES

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # return 2
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # return 1

# n = 4
# computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]] # return 1

'''

'''
풀이2 : BFS
- testcase는 다 통과하지만
- 채점 결과 2, 5번만 정답
'''

'''
def solution(n, computers):

    visited = [ [False] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs(x, y, computers, visited):
        q = deque([(x, y)])
        while q :
            x, y = q.popleft()
            visited[x][y] = True

            for d in range(len(dx)):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < len(computers):
                    if visited[nx][ny] == False and computers[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))

        return

    answer = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == False:
                bfs(i, j, computers, visited)
                answer += 1    

    return answer
'''



'''
풀이1 : DFS
- 그래프 연결이 끊길 때 네트워크 개수 +1
- 섬의 개수 세기 문제와 동일?
- 채점 결과 2, 5번만 정답
'''

'''
def solution(n, computers):
    
    # 시계 방향으로 회전 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

    answer = 0 # network count
    visited = [ [False]* n for _ in range(len(computers)) ]

    def dfs(x, y):
        visited[x][y] = True

        for d in range(len(dx)):
            nx = x + dx[d]
            ny = y + dy[d]
            # if nx < 0 or ny < 0 or nx >= n or ny >= len(computers):
            #     continue
            if 0 <= nx < n and 0 <= ny < len(computers):
                if visited[nx][ny] == False and computers[nx][ny] == 1:
                    dfs(nx, ny)

        return

    for i in range(n):
        for j in range(len(computers)):
            if visited[i][j] == False and computers[i][j] == 1:
                dfs(i, j)
                answer += 1                           

    return answer
'''

