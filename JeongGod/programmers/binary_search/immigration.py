def solution(n, times):
    '''
    최대 10억으로 잡고 mid값을 구한다.
    mid값일 때 심사관들이 몇 명의 사람을 처리할 수 있는지 판단한다.
    1. target < n
        mid를 키운다.
    2. target >= n
        mid를 줄인다.
    '''

    left, right = 1, n*max(times)
    while left <= right:
        mid = (left+right) // 2
        # mid에서 몇 명을 처리할 수 있는지
        target = sum(mid // t for t in times)
        if target < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
