from string import ascii_uppercase

'''
풀이
1. 알파벳 값에 대응하는 사전을 만듭니다.
{'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
2. 이름 오른쪽에 A가 있다면 왼쪽으로 이동하고, 없다면 오른쪽으로 이동하며 탐색합니다.

** 현재 코드는 테스트 케이스 10, 11에서 오류가 발생합니다. 
name = "ZZZAAAZ" 는 방향을 도중에 한 번 바꾸면 9기 나와야 하는데 저는 방향을 바꾸는 것을 고려하지 않았으므로 10을 리턴하고 있습니다.
'''
# 알파벳 : 숫자 값 사전 만들기
def make_dict():
    alpha_dict = dict()
    for idx, alpha in enumerate(list(ascii_uppercase)):
        if idx <= 13:
            alpha_dict[alpha] = idx
        else:
            alpha_dict[alpha] = 26 - idx
    
    return alpha_dict


def solution(name):
    answer = 0

    if set(list(name)) == {"A"}:
        return 0

    alpha_dict = make_dict()

    right_answer = 0
    left_answer = 0

    for idx, n in enumerate(name):
        if idx!= 0:
            right_answer += 1
        if n != "A":
            right_answer += alpha_dict[n]
   
    for i in range(0, -(len(name)), -1):
        if name[i] != "A":
            plus = alpha_dict[name[i]] + 1 if i != 0 else alpha_dict[name[i]]
            left_answer += plus
        else:
            plus = 1 if i != -(len(name)-1) else 0
            left_answer += plus
    
    
    answer = min(left_answer, right_answer)
    
    return answer
