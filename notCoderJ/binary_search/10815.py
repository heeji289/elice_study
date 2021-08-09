'''
    풀이 요약
        음... 이 문제는 주어진 입력의 수가 최대 50만이고 중복되는 숫자 카드가 없으므로
        간단히 집합 자료형을 이용한 순차 탐색으로 해결할 수 있다고 생각했습니다.
        하지만, 이번주의 취지가 이분 탐색 알고리즘 능력을 향상시키기 위함이므로 이분 탐색을 구현해서도 풀어봤습니다.
        총 3가지의 풀이 방식으로 풀었습니다.
        
        1. 집합 자료형을 이용한 순차 탐색 풀이
            n개의 숫자에 대한 집합을 만들고 주어지는 m개의 숫자를 하나씩 순회하며 해당 집합에 들어있는지 확인하여 0 또는 1을 출력합니다.
            
        2. 직접 이분 탐색을 구현한 풀이
            처음에는 이분 탐색 함수에 리스트를 슬라이싱하여 분할된 리스트를 매개 변수로 전달하는 방식으로 구현헀는데
            슬라이싱 과정에서 시간이 많이 소요되어 시간 초과 판정을 받았습니다.
            그래서 이분 탐색 함수에 시작, 끝 인덱스를 전달하고 해당 인덱스를 통해 중간 인덱스를 구하여 탐색하는 방법으로 다시 구현했습니다.
            이 방법은 통과는 되었으나, 이분 탐색임에도 1번 알고리즘보다 효율성이 많이 떨어지더라구요... 아마 초기에 n개의 숫자를 정렬해야하기 때문인 것 같습니다.
            
        3. 이분 탐색 모듈(bisect)를 이용한 풀이
            bisect 모듈을 간단히 설명하면
                - bisect_left(리스트, 대상 값) : 매개 변수로 주어진 정렬된 리스트에 대상 값이 들어갈 좌측 인덱스를 반환합니다.
                - bisect_right(리스트, 대상 값) : 매개 변수로 주어진 정렬된 리스트에 대상 값이 들어갈 우측 인덱스를 반환합니다.
                ex) a = [1, 2, 6, 10]이 있을 때 bisect_left(a, 2) = 1 / bisect_right(a, 2) = 2를 반환합니다.
            위처럼 반환되는 값을 이용해 좌측 != 우측인 경우 값이 존재한다고 판단하고, 좌측 == 우측인 경우 값이 존재하지 않는다고 판단하여 풀이했습니다.
'''
from bisect import bisect_left, bisect_right
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(500001)


def bSearch(target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        return bSearch(target, start, mid - 1)
    else:
        return bSearch(target, mid + 1, end)


def lib_bSearch(target, nums):
    if bisect_left(nums, target) != bisect_right(nums, target):
        return True
    else:
        return False
    

if __name__ == "__main__":
    n = int(input())
    # nums = set(input().split())
    nums = sorted(list(map(int, input().split())))
    m = int(input())
    
    # for i in input().split():
    #     print(1) if i in nums else print(0)
    
    # for i in map(int, input().split()):
    #     print(1) if bSearch(i, 0, n - 1) else print(0)
    
    for i in map(int, input().split()):
        print(1) if lib_bSearch(i, nums) else print(0)