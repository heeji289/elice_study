# N과 M (1)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 숫자를 사용했는지 여부를 나타냄 (수열을 만들 때)
visited = [False] * (n + 1)
# 수열 정보를 저장할 배열 [1, 3, 4] 형식 
arr = [0] * m

# idx = 수열에서 어느위치의 값을 정할 것인지 가리킴
# 어떤 수열의 idx번째의 수를 결정한다
def solve(idx, n, m):
    # 수열이 결정된 순간이므로 출력
    if idx == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, n + 1):
        if visited[i]: continue # 이미 선택된 숫자이므로 continue
        visited[i] = True
        arr[idx] = i # 해당 인덱스의 값을 갱신
        solve(idx + 1, n, m) # 다음 인덱스 값을 찾기 위해 재귀 호출
        # 위에서 visited[i]가 True인 경우에 만들 수 있는 수열을 다 처리했으므로
        # 다시 방문하지 않았다고 표시해줌
        visited[i] = False

solve(0, n, m)
