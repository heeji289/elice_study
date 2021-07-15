# 문자열 집합

'''
[문제]
문자열 N개가 주어진다 (=집합 S)
찾을 문자열 M개가 주어질 때, 이 중 집합S에 포함되는 것이 몇 개인지 구해라.

[풀이]
집합S를 딕셔너리로 생성 -> 문자열M이 딕셔너리의 key에 존재하면 정답 +1을 해준다.
'''
import sys

n, m = map(int, sys.stdin.readline().split())

arrInSet = []
arrToFind = []
answer = 0

for _ in range(n):
    arrInSet.append(sys.stdin.readline().rstrip())

for _ in range(m):
    arrToFind.append(sys.stdin.readline().rstrip())

_set = {}

for item in arrInSet:
    _set[item] = True

for _str in arrToFind:
    if _str in _set.keys():
        answer += 1


print(answer)

