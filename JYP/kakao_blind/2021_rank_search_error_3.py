from collections import deque

def solution(info, query):

    # query preprocessing
    requirements = []
    for q in query:
        q_list = deque(q.split())
        base_score = 0
        while q_list:
            if q_list[0] == "and" or q_list[0] == "-":
                q_list.popleft()

            # score is the last element    
            elif q_list[0].isnumeric():
                base_score = int(q_list.popleft())
                break
            else:
                q_list.rotate(-1)
                
        requirements.append([set(q_list), base_score])

        
    
    # info preprocessing
    applicants = []
    for person in info:
        person_info = person.split()
        score = int(person_info[-1])
        applicants.append([set(person_info[:-1]), score])
        
        
    # filtering
    answer = []
    for r in requirements:
        sum = 0
        for applicant in applicants:
            if applicant[1] >= r[1] and len(r[0] - applicant[0]) == 0:
                sum += 1
        answer.append(sum)


    return answer