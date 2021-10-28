import re
from collections import defaultdict

''' 
testcase 6~9번 틀리는 코드입니다.
'''

# tail은 정렬할 때 고려사항이 아님
def solution(files):
    answer = []
    file_dict = defaultdict(list)

    for idx, file in enumerate(files):
        # 헤드가 공백으로 시작하거나 특수기호인 경우를 고려하여 추가 전처리 (test cast 6-9...)
        for i, f in enumerate(file):
            if f != ' ':
                file = file[i:]
                break
        
        head =  re.sub("[0-9]", " ", file).split(' ')[0].lower()
        # print(head)


        # 숫자가 두 번 나오는 부분 처리를 위해 for문 추가
        number = re.sub("[^0-9]"," ", file).split(' ')
        for num in number:
            if num != "":
                number = num
                break

        # 숫자는 5자리까지이므로 5자리 초과는 tail 취급
        file_dict[head].append([int(number[:5]), idx])
        
    
    for _, val in sorted(file_dict.items()):
        for _, idx in sorted(val):
            answer.append(files[idx])

    return answer



'''
# re.split을 쓸 생각을 못했네요, 6-9번 테케 해결하려다가 이 풀이를 봐버렸습니다..ㅎㅎ;

def solution(files): 
    answer = [] 
    
    head_num_tail = [re.split(r"([0-9]+)", file) for file in files] 
    
    sorted_head_num_tail = sorted(head_num_tail, key=lambda x: (x[0].lower(), int(x[1]))) 
    
    answer = ["".join(h_n_t) for h_n_t in sorted_head_num_tail] 
    
    return answer

출처: https://somjang.tistory.com/entry/Programmers-2018-KAKAO-BLIND-RECRUITMENT-3차-파일명-정렬-Python
'''



# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

# files = ['abc124.jpg', 'abc123defg123.jpg', ' ab34.jpg', '-30.jpg']
