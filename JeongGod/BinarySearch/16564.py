'''
N개의 캐릭터, 각 캐릭터의 레벨은 Xi
레벨을 총합 K만큼 올릴 수 있다.
가장 작은 레벨을 최대로 끌어올리고 싶다.

N = 1,000,000
sort가능. nlogn
작은 레벨을 찾고, 1씩 올린다.
1씩 올리면 1억번 연산이 이루어진다. 안돼.
2초면 가능할거같다.
100*1억번의 연산
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
characters = []
for i in range(n):
    characters.append(int(input()))

characters.sort()
length = 1
ans = 0
# 10 15 20 // 10
for i in range(n-1):
    # length개의 캐릭터들을 nam만큼 올릴 수 있는 정도
    nam = k // length
    diff = characters[i+1] - characters[i]
    # 옆에 있는 캐릭터만큼 나머지 캐릭터도 올릴 수 있다면
    if diff < nam:
        characters[i] += diff
        k -= diff*length
    # 만약 옆 캐릭터만큼 올릴 수 없다면, 남은 캐릭터들의 레벨을 올린다.
    else:
        characters[i] += nam
        break
    length += 1

print(characters[i])

######################################################
# 백준 pypy효율성 1등 풀이
import sys

def total(lists, mid):
    tmp_k = 0
    for xi in lists:
        if xi >= mid:
            return tmp_k
        tmp_k += (mid-xi)
    return tmp_k

# N은 캐릭터의 개수, K는 현재 내가 올릴 수 있는 레벨
N, K = map(int, sys.stdin.readline().split())
X = sorted([int(sys.stdin.readline()) for _ in range(N)])

# X와 X가 커질 수 있는 최댓값
start, end = min(X), min(X) + K
answer = 0
while start <= end:
    mid = (start+end)//2
    if total(X, mid) <= K:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)