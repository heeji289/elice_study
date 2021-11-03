import math
import re
from collections import deque

'''
풀이
1. 전처리
- 알파벳 소문자만 남기고 모두 공백으로 치환합니다.
- 연속된 글자 2개를 가져와서 둘 다 알파벳이라면 리스트에 추가합니다. 
- 리스트에 추가할 때 중복 여부를 확인하지 않으면 자동으로 다중집합이 생성됩니다.

2. 다중집합 합집합 만들기
- b 집합의 원소가 a 집합에 없다면 결과에 추가해주고
- b 집합의 원소가 a 집합이 있다면 결과에 추가하지 않으며 a 집합에서도 제거합니다. 
- 이때 copy 메서드를 사용하지 않으면 결과에 오류가 발생합니다. (참조만 하는 것이 아니라 실제 값을 복사해야 함 - 얕은복사 가능)

3. 다중집합 교집합 만들기
- b 집합의 원소가 a 집합에 있다면 결과 리스트에 추가합니다. 

4. 결과
- 문제의 지시대로 교/합 나눗셈 결과에 65536을 곱하고 소수점 이하 버림을 하여 정수 결과를 반환합니다.
'''

def preprocessing(str):
    new_str = re.sub(r'[^a-z]',' ',str.lower())
    new_str = re.sub(r'[0-9]',' ',new_str)

    result = []
    for i in range(len(new_str)-1):
        elem = ''.join(new_str[i:i+2])
        if elem.isalpha():
            result.append(elem)

    return result

# multiset union 다중집합 합집합
def make_union(a, b):
    a_temp = deque(a.copy())
    a_result = a.copy()

    for b_elem in b:
        if b_elem not in a_temp:
            a_result.append(b_elem)
        else:
            del a_temp[a_temp.index(b_elem)]

    return a_result


# multiset intersection 다중집합 교집합
def make_intersection(a, b):
    a = deque(a)
    result = []
    for b_elem in b:
        if b_elem in a:
            del a[a.index(b_elem)]
            result.append(b_elem)
    
    return result


def solution(str1, str2):
    answer = 0
    
    str1 = preprocessing(str1)
    str2 = preprocessing(str2)

    len_union = len(make_union(str1, str2))
    len_inter = len(make_intersection(str1, str2))
    
    if len_union == 0:
        result = 1
    else:
        result = len_inter / len_union
    
    answer = math.trunc(result * 65536)

    return answer
