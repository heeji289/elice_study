from collections import deque

def iscorrect(w):
    w = deque(w)
    correct = []
    incorrect = []

    while w:
        if not incorrect or w[0] == "(":
            incorrect.append(w.popleft())
        elif incorrect and incorrect[-1] == "(" and w[0] == ")":
            correct.append(incorrect.pop())
            correct.append(w.popleft())
        else:
            incorrect.append(w.popleft())

    return not incorrect


def divide(w):
    open_ = 0
    close_ = 0

    for idx, w_ in enumerate(w):
        if w_ == "(":
            open_ += 1

        elif w_ == ")":
            close_ += 1

        if open_ == close_:
            return w[:idx+1], w[idx+1:]


def solution(p):
	# 1번 로직
    if iscorrect(p):
        return p

    # 2번 로직
    u = divide(p)[0]
    v = divide(p)[1]
		
	# 3번 로직
    if iscorrect(u):
        v_ = solution(v)
        return u + v_

	# 4번 로직
    elif not iscorrect(u):
        before_u = u[1:-1]
        after_u = ""
        for i in range(len(before_u)):
            if before_u[i] == ")":
                after_u += "("
            elif before_u[i] == "(":
                after_u += ")"

        return "(" + solution(v) + ")" + after_u