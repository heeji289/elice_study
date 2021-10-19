'''
  풀이요약
  1. 0부터 각 수를 주어진 진법으로 변환한 후 문자열로 nums에 추가해줍니다.
  2. nums의 길이가 m과 같거나 큰 경우 nums의 p-1번째 값을 answer에 추가해주고 구할 숫자의 갯수를 1 감소시킵니다.
  3. 위 과정을 반복한 후 구할 숫자의 갯수가 남지 않으면 answer를 반환합니다.
'''

import string

def solution(n, t, m, p):
    answer = ''
    conv = list(string.digits) + ['A', 'B', 'C', 'D', 'E', 'F']

    def base_n(a, b, c):
        if not a:
            return '0' if not c else c
        return base_n(a // b, b, conv[a % b] + c)
    
    remain = t
    nums = ''
    for i in range(99999999999999999999):
        if len(nums) >= m:
            answer += nums[p - 1]
            remain -= 1
            nums = nums[m:] # m개보다 클 경우 m개 이후 숫자를 남김
            if not remain:
                return answer
        nums += base_n(i, n, '')