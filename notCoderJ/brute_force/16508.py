'''
    풀이 요약:
        으악 코드 너무 지저분해요...
        일단 생각한 로직은 주어지는 전공책들을 1 ~ n개까지 선택하는 조합들을 싹다 구한 후
        각 조합의 가격을 합치고 제목들을 합칩니다. 이후 각 제목들과 만들고자하는 문자열의 알파벳이
        모두 겹치는 케이스에서만 만들고자하는 문자열의 각 알파벳 수를 충족하는 지 확인하여 저렴한 가격으로 갱신해나가는 코드입니다.
'''

from itertools import combinations
from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()

INVALID = 16_00_001


answer = INVALID
t = input()
n = int(input())
major = [input().split() for _ in range(n)]
str_len = len(t)

# 전공책들의 각 조합에서 가격의 합과 제목의 합을 구하는 함수
def parse_books(books):
    cost, titles = 0, ''
    for c, t in books:
        cost += int(c)
        titles += t
    return cost, titles

for i in range(1, n + 1):
    for books in combinations(major, i):
        cost, titles = parse_books(books)
        if not set(t) - set(titles): # 만들고자하는 문자열의 알파벳들이 전공책들 제목합의 알파벳들과 모두 겹치는지 체크
            valid = True
            alphas = dict(Counter(titles))
            for k, v in Counter(t).items():
                if alphas[k] < v:
                    valid = False
                    break
            if valid:
                answer = min(answer, cost)

print(answer if answer != INVALID else -1)