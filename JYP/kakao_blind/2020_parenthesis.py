def iscorrect(w):

    balance = 0
    for w_ in w:
        if w_ == "(":
            balance += 1
        else:
            if balance == 0:
                return False
            balance -= 1

    return True


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