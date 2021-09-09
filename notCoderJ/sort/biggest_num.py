'''
  풀이요약
    주어진 숫자를 문자로 변환하여 문자를 기준으로 정렬하여 풀이했습니다.
    1. 주어진 숫자를 단순히 문자로 변환해서 정렬하면 94, 99, 9 이런 숫자가 들어올 경우 99, 94, 9 이렇게 정렬이 되는데
      가장 큰수는 99 9 94와 같은 순서이므로 모든 숫자에 대해 자릿수를 동일하게 맞춰 문자열로 변환 후 정렬해줍니다.
    2. 정렬한 수에서 원래 자릿 수만큼의 문자열 형태 숫자를 빼와서 합치고 int로 변환 후 다시 문자열로 변환해서 반환해줍니다.
      int로 한번 변환했다가 str로 다시 변환하는 이유는 0, 0, 0, 0 같은 경우 '0'으로 정상 반환하도록 하기 위함입니다.
      이부분을 몰라서 계속 실패하다가 질문 게시판을 통해 알게 됬습니다ㅎㅎ
'''

def solution(numbers):
    nums = sorted([((str(n) * 4)[:4], len(str(n))) for n in numbers], reverse=True)
    return str(int(''.join(map(lambda x: x[0][:x[1]], nums))))
  
  

# 다른 분의 풀이를 보니 더 간단한 방법이 있었네요 ㅎㅎ
# 먼저 문자로 바꾼후 자리 수를 충분히 크게 잡은 수로 정렬만 해서 합치는 방법도 잇네요.
# 굳이 4를 곱하지 않고 3만 곱해줘도 1000이 마지막 숫자라 충분히 비교가 되는군요.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 이분의 풀이를 보고 제 코드를 개선해봤습니다.
def solution(numbers):
    return str(int(''.join(sorted([str(n) for n in numbers], key=lambda x: x*3, reverse=True))))