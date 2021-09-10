from collections import deque

def solution(info, query):

    # query preprocessing
    requirements = []
    for q in query:
        deq = deque(q)
        q_list = set()
        base_score = ""
        word = ""
        while deq:
            if deq[0].isalpha():
                word += deq[0]
                deq.popleft()
            elif deq[0] == " ":
                if word == "and":
                    word = ""
                elif word != "":
                    q_list.add(word)
                    word = ""
                deq.popleft()
            elif deq[0].isnumeric():
                base_score += deq[0]
                deq.popleft()
            else:
                deq.popleft()
        
        requirements.append([q_list, int(base_score)])

         
    
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