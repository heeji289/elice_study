'''
  풀이 요약
    1부터 최대 반복가능한 문자열의 길이인 전체 문자열 길이의 반만큼 순회하면서
    현재 값만큼의 길이를 갖는 반복할 문자열을 만들고 해당 문자열과 일치하는 문자열이 있는 경우 카운트합니다.
    일치하는 문자열이 없는 경우 카운트 값에 따라
    현재 반복 문자열 or str(카운트 값) + 현재 반복 문자열을 압축한 문자열에 추가해주고
    반복 문자열과 카운트 값을 초기화해줍니다.
    압축한 문자열의 길이와 이전 압축 문자열의 길이를 비교해서 작은 값을 answer에 넣습니다.
'''

def solution(s):
    answer = 1001
    for i in range(1, (len(s) // 2) + 1):
        start, cnt = 0, 1
        iter, string = '', ''
        while start < len(s):
            if len(iter) < i:
                iter += s[start]
                start += 1
            elif iter == s[start:start + i]:
                cnt += 1
                start = start + i
            else:
                string += (iter, str(cnt) + iter)[cnt > 1]
                iter = ''
                cnt = 1
        answer = min(answer, len((string + iter, string + str(cnt) + iter)[cnt > 1]))
    
    return answer if len(s) != 1 else 1