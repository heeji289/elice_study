from collections import deque, Counter

def solution(info, query):

    # query preprocessing
    requirements = []
    for q in query:
        que = deque(sorted(Counter(q.split())))
        while que:
            if que[0] == '-':
                que.popleft()
            elif que[0].isnumeric():
                base_score = que[0]
                que.popleft()
            elif que[0] == 'and':
                que.popleft()
                break

        requirements.append([set(que), int(base_score)])
    
    applicants = []
    for p in info:
        person = deque(sorted(Counter(p.split())))
        score = int(person[0])
        person.popleft()
        applicants.append([set(person), score])

    
    answer = []
    for r in requirements:
        sum = 0
        for applicant in applicants:
            if applicant[1] >= r[1] and len(r[0] - applicant[0]) == 0:
                sum += 1
        answer.append(sum)
        
    return answer