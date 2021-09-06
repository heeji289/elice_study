# 전공책

"""
순서 상관없이 단어만 찾아서 뽑으면 되는 듯?

[입력]
만들고자 하는 단어 T (10개 이하)
전공책의 수 N (16개 이하)
각 줄에 전공책의 가격 C와 제목 W

단어를 만들 때 가장 적은 가격의 합을 출력
단어를 만들 수 없으면 -1

[생각]
1. 전공책의 제목에 있는 문자를 키로, 책 가격을 값으로 두는 딕셔너리를 만들어서 가장 작은 값만 저장한다.
books_str = {"문자" : "책 번호"}
books_price = {"책 번호" : "가격"}
2. 만들고자 하는 단어를 딕셔너리에서 하나씩 찾고 book_number 집합에 저장! (가격이 제일 저렴한 걸로)

*** 잘못된 생각.. 찾고자 하는 단어가 책 하나에 존재하면 로직이 맞지 않음..
"""
import sys
input = sys.stdin.readline

# T 입력
T = input().rstrip()
# N 입력
n = int(input())
# books_price = {"책 번호" : "가격"}으로 저장
books_price = {}

# price, title 입력
for _ in range(n):
    price, title = input().rstrip().split()
    books_price[title] = price

# books_str = {"문자" : [책 번호]}로 저장 => 인접리스트로 변경.. 그냥 책 이름 넣자
books_str = [[] for _ in range(26)]  # 알파벳 개수만큼

for book_num, (title, price) in enumerate(books_price.items()):
    for _str in set(title):
        asc_str = ord(_str)
        asc_A = ord('A')
        new_idx = asc_str - asc_A
        # 해당 문자 인접리스트에 책 제목을 삽입
        books_str[new_idx].append(title)

# 문자열 T의 요소에 반복문으로 접근
# books_str에서 해당 문자가 존재하는 책 번호를 찾고
# 찾은 책 번호들 중 가장 값이 적게 드는 책의 번호를 books_number = set()에 저장
# 나중에는 books_number에 있는 책의 가격을 더해준다.

# 여기부분 작성하다가 틀림을 느끼고 다시 생각..
answer = set()

for item in T:
    idx = ord(item) - ord('A')
    min = 1000000
    find = ""
    for i in books_str[idx]:
        if min > books_price[i]:
            min = books_price[i]
            find = i
    
    print(find)