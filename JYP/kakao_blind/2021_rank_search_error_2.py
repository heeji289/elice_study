def solution(info, query):

    requirements = []

    # query 
    answer = []
    for q in query:
        q_list = q.replace('and', ' ').replace('-', '').split()
        base_score = int(q_list[-1])
        requirements = q_list[:-1]
        sum = 0
        for val in info:
            applicant = val.split(' ')
            score = int(applicant[-1])
            if score >= base_score and len(set(requirements) - set(applicant[:-1])) == 0:
                sum += 1
        answer.append(sum)

	return answer