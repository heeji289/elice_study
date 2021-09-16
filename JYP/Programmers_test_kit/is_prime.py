# Brute Force

from itertools import permutations

def solution(numbers):
    # initialization
    nums = [i for i in numbers]

    def unpack_and_make_digit(tu):
        tuple_to_list = list(tu)
        num = ""
        for s in tuple_to_list:
            num += s
        return int(num)
    
    # make permutations
    perm = []
    for i in range(1,len(nums)+1):
        # 특이하게도, "011"로 만든 1과 1, 11과 11은 서로 다른 메모리주소여서 그런지 set을 해도 다른 원소로 인식됩니다.
        # set 결과 {0, 1, 1, 11, 11, ... } 이런건 처음 봤네요.;
        # 그래서 필터링 코드를 아래 result 부분에 추가했습니다.
        perm.extend(list(map(unpack_and_make_digit, permutations(nums, i))))
    
    result = []
    [result.append(n) for n in perm if n not in result and n != 0 and n!= 1]

    
    cnt = 0
    for n in result:
        flag = False
        for i in range(2, n):
            if n % i == 0:
                flag = True
                break
        
        if not flag:
            cnt += 1


    return cnt
