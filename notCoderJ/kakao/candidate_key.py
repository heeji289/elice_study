'''
  풀이 요약
    bitmask를 이용해서 풀었습니다.
    bitmask 문제 풀이가 어떤 방식인지 제대로 풀어본적이 없어서 이런식으로 쓰는게 맞나 싶네요...
    
    1. 먼저 컬럼의 모든 조합의 수만큼 True 값으로 후보키 리스트를 초기화해줍니다.
    2. bitmask를 1부터 최대 조합의 수까지 순회하며 현재 bitmask의 후보키 값을 확인합니다.
    3. 만약 후보키 값이 True인 경우 relation을 하나씩 돌며 현재 bitmask 내 '1'인 부분에 해당하는 컬럼들만 뽑아서 튜플을 집합에 넣어줍니다.
      3-1. 중복 튜플이 발생하는 경우 현재 bitmask에서의 후보키 값을 False로 변경합니다.
      3-2. 중복 튜플이 없는 경우 현재 bitmask보다 1 큰 값부터 최대 조합의 수까지 순회하며 현재 bitmask를 포함하는 조합들에서의 후보키들을 False로 변경해줍니다.
    4. 후보키 리스트에서 True인 값들만 카운트하여 반환합니다.
'''

def solution(relation):
    mask_len = 2 ** len(relation[0])
    
    # 0000 0000
    keys = [True for _ in range(mask_len)]
    keys[0] = False
    
    for mask in range(1, mask_len):
        if keys[mask]:
            items = set()
            for tp in relation:
                item = tuple([tp[i] for i, v in enumerate(bin(mask)[2:][::-1]) if v == '1'])
                if item in items:
                    keys[mask] = False
                    break
                items.add(item)
            else:
                for i in range(mask + 1, mask_len):
                    if mask & i == mask:
                        keys[i] = False

    return keys.count(True)