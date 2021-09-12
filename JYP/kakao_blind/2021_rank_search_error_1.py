# error case 1
from collections import defaultdict

def solution(info, query):

    criteria = []
    requirements = []

    # query 
    for q in query:
        q_list = q.replace('and', ' ').replace('-', '').split()
        criteria.append(int(q_list[-1]))
        requirements.append(q_list[:-1])


    answer = []


    # info search
    for idx, base_score in enumerate(criteria):
        sum = 0
        for val in info:
            applicant = val.split(' ')
            score = int(applicant[-1])
            if score >= base_score and len(set(requirements[idx]) - set(applicant[:-1])) == 0:
                sum += 1
        
        answer.append(sum)



    return answer