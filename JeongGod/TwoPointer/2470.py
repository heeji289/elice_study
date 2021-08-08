'''
<내 풀이>
용액을 절댓값순으로 정렬한다.
2개의 용액씩 비교하면서 제일 작은 값을 저장하면서 끝까지 간다.


<투포인터 형식 풀이>
용액을 오름차순으로 정렬한다.
맨 왼쪽 용액과, 맨 오른쪽 용액을 처음 고른다. 그리고 그의 합을 구한다.
만약 합이 음수라면
    => 맨 왼쪽용액이 더 크다는 얘기. 그래서 왼쪽 용액을 작은애로 골라서 그 차이를 줄여본다.
만약 합이 양수라면
    => 맨 오른쪽 용액이 더 크다는 얘기. 그래서 오른쪽 용액을 더 작은애로 골라 그 차이를 줄여준다.
'''
import sys
input = sys.stdin.readline

n = int(input())

_list = sorted(list(map(int, input().split())), key = lambda x : abs(x))

ans = sys.maxsize
for i in range(len(_list)-1):
    if abs(_list[i] + _list[i+1]) < ans:
        ans = abs(_list[i] + _list[i+1])
        x, y = _list[i], _list[i+1]

print(*sorted([x,y]))
