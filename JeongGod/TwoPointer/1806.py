import sys
input = sys.stdin.readline

n, target = map(int, input().split())
# a = input()
_list = list(map(int, input().split()))

part_len = 0
ans = sys.maxsize
start = 0
part_sum = 0
# 10만
for i in range(len(_list)):
    # 값이 작다면 더한다.
    if part_sum < target:
        part_sum += _list[i]
        part_len += 1
    # 값이 크다면 맨 앞에 있는 수를 빼준다.
    while part_sum >= target and start <= i:
        ans = min(ans, part_len)
        part_sum -= _list[start]
        part_len -= 1
        start += 1

print(ans if ans != sys.maxsize else 0)