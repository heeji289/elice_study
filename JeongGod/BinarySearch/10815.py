'''
숫자카드 N개 가지고 있다.
M개가 주어졌을 때, 이 수가 숫자카드에 있는지 없는지 판단

N = 500,000
M = 500,000
'''
import sys
input = sys.stdin.readline

N = int(input())
N_li = sorted(list(map(int, input().split())))

M = int(input())
M_li = list(map(int, input().split()))

def search(num):
    left, right = 0, len(N_li)-1
    while left <= right:
        mid = (left+right)//2
        if N_li[mid] < num:
            left = mid+1
        elif N_li[mid] > num:
            right = mid-1
        else:
            return 1
    return 0

for elem in M_li:
    print(search(elem), end = " ")
print("")