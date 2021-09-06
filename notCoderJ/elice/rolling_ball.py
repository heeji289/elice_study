'''
    풀이 요약
        테스트때는 반복구간에 대해 제대로 생각하지 못해서 다음 좌표가 이전 좌표가 될 경우만 있다고 생각하고 스택으로 접근했습니다.😅
        물론 스택으로 풀어도 해당 좌표가 스택에 있는 지 검사하는 방법으로 풀 수 있다고 생각은 합니다.
        하지만, 다시 풀어볼 때는 dfs를 이용한 방법으로 푸는 것이 더 깔끔할 것 같다고 생각하여 dfs로 풀어봤습니다.
        
        기저 조건
            1. 현재 좌표가 구간을 벗어났으면 -1을 반환하고 종료
            2. 현재 좌표를 방문한 적이 있다면 현재 좌표까지의 길이(i) - 방문 좌표까지의 길이(해당 방문 좌표를 key로 하는 값)
        기저 조건에 해당하지 않으면 현재 좌표를 key로, 현재까지의 길이를 value로 해서 딕셔너리에 저장하여 방문처리하고
        다음 이동 좌표에 대해 dfs 수행을 반복합니다.
'''
def main():
    n, m = map(int, input().split())
    dirs = {'1': (-1, 0), '2': (0, -1), '3': (0, 1), '4': (1, 0)}
    maps = [''] + [[''] + input().split() for _ in range(n)]
    y, x = map(int, input().split())
    
    
    def repeatCnt(y, x, i, visited):
        if y < 1 or y > n or x < 1 or x > m:
            return -1
            
        if (y, x) in visited:
            return i - visited[(y, x)]
        
        visited[(y, x)] = i
        dy, dx = dirs[maps[y][x]]
        return repeatCnt(y + dy, x + dx, i + 1, visited)

    print(repeatCnt(y, x, 1, dict()))


if __name__=="__main__":
    main()