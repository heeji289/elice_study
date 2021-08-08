import sys
input = sys.stdin.readline

n, m = map(int, input().split())

_list = [0] + list(map(int, input().split()))

for i in range(1, len(_list)):
    _list[i] = _list[i-1]+_list[i]

for _ in range(m):
    i,j = map(int, input().split())
    print(_list[j]-_list[i-1])