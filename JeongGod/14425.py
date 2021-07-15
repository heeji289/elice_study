import sys
n, m = map(int, sys.stdin.readline().split())
ans = 0

_set = set()
for _ in range(n):
    _set.add(sys.stdin.readline().rstrip())

for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp in _set:
        ans += 1

print(ans)