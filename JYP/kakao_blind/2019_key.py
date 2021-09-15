#relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations
def solution(relation):
    row = len(relation) # 행
    col = len(relation[0]) # 열
    cols = [i for i in range(col)]

    # 선택할 컬럼의 조합의 경우의 수 구하기
    # 예 : (0), (1), (2), (3), (0, 1), (0, 2), ... , (0, 1, 2, 3)
    # combination배열의 차원을 늘리지 않기 위해 extend로 추가
    combination = []
    for i in range(1, col+1):
        combination.extend((combinations(cols, i)))  
    

    # 유일성 체크

    # 다중 for문
    # col * row <= 160이므로, 
    # for를 조금 과도하게 돌아도 시간복잡도, 메모리 이슈는 없을 것 같아서 그냥 했습니다.
    unique = []
    for combi in combination:
            # 이 부분을 리스트 컴프리헨션으로 작성하지 않으면 배열의 차원이 증가해서 이렇게 두었습니다.(*확인필요)
            # 조합 패턴에 맞게 데이터를 다시 튜플로 모아줍니다.
                # 예를 들어 combi = (0, 1)인 경우, 
                # temp = [('100', 'ryan'), ('200', 'apeach'), ... , ('600', 'apeach')] 
                # 원래 데이터의 0행과 1행을 선택한 조합이 됩니다.
            temp = [tuple([data[c] for c in combi]) for data in relation]
            
            # temp를 집합으로 만들었을 때 전체 행의 수와 같으면 유일성을 만족한다고 판단합니다.
            if len(set(temp)) == row:
                unique.append(combi)

    
    # 최소성 체크
    # result에는 유일성을 만족하는 조합방법(레시피?!)을 담은 튜플이 있음(정렬은 안 된 상태)
    # 예 : {(0, 1), (1, 2), (0, 1, 2), ... (0, 1, 2, 3), (0)}
        # 여기서 (0, 1)과 (0, 1, 2), (0, 1, 2, 3)은 모두 (0, 1)을 포함하므로 뒤의 2개 튜플은 리스트에서 삭제하기
        # 삭제할 때 remove를 쓰면 없는 요소를 지우려고 할 때 에러가 생기니 discard 권장
        # 리스트 요소 삭제는 시간복잡도 이슈로 바람직하지 않다고 알고 있으나 테스트케이스 기준 result의 데이터 개수가 10개여서 별 무리 없을 것이라 판단함
    result = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)): 
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                result.discard(unique[j])
        

    return len(result)


#print(solution(relation))