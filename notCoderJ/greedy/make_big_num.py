'''
  풀이요약
    스택을 이용해서 이전 숫자와 현재 숫자를 비교하며 k가 0이 되거나 주어진 모든 숫자를 순회할 때까지 큰 값을 남기는 방법으로 풀었습니다.
    1. 주어진 숫자들을 순회하면서 stack에 숫자를 하나씩 넣고 현재 숫자와 stack에 들어있는 숫자를 비교합니다.
    2. 만약 stack에 들어있는 숫자가 현재 숫자보다 작으면서 제거할 수 k가 남아 있는 경우 stack의 숫자를 하나씩 꺼내고 k를 1 감소시킵니다.
    3. 위 과정을 모두 수행한 후 k가 남아 있으면 뒤에서부터 k만큼 숫자를 제거한 후 반환합니다.
'''

def solution(number, k):
    stack = []
    for i in number:
        while stack and k != 0:
            if stack[-1] < i:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    return ''.join(stack[:len(stack)-k])