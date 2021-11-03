import string
from collections import Counter


def solution(str1, str2):
    """
    2개씩 문자열을 묶는다.
    만약 문자열에 특수문자가 들어가있다면 버린다.

    중복을 허용한다. Counter를 이용한다.
    개수가 작은것끼리 교집합
    개수가 큰 것끼리 합집합

    1. 일단 문자열을 2개씩 쪼개서 리스트화한다.
    => str.lower사용, 특수문자는 버린다.
    2. 리스트를 Counter로 만들어 개수를 센다.
    3. 개수가 작은것으로는 교집합, 개수가 큰 것으로는 합집합
    4. 자카드 유사도를 구한다. 교집합 / 합집합
    5. 자카드 유사도에서 65536을 곱한다. => int형으로 출력한다.

    * 합집합이 없는 경우는 1로 출력
    """

    answer = 0

    def two_string(input_str):
        alpha = set(string.ascii_lowercase)
        tmp = []
        for i in range(len(input_str)-1):
            two_str = (input_str[i] + input_str[i+1]).lower()
            # 특수문자가 포함되어있으면 없앤다.
            if two_str[0] not in alpha or two_str[1] not in alpha:
                continue
            tmp.append(two_str)
        return tmp

    cnt_str1 = Counter(two_string(str1))
    cnt_str2 = Counter(two_string(str2))

    # 교집합의 개수를 구한다.
    inter = 0
    for key, value in cnt_str1.items():
        str2_val = 0 if cnt_str2.get(key) is None else cnt_str2.get(key)
        inter += min(str2_val, value)
    # 합집합의 개수를 구한다. A + B - A ^ B
    union = sum((cnt_str1 + cnt_str2).values()) - inter
    if union == 0:
        return 65536

    return int((inter / union) * 65536)
