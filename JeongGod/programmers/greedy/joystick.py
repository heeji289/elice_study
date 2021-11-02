import string


def solution(name):
    """
    최소한의 움직임을 해야한다.
    총 26개의 알파벳
    0 ~ 12까지는 다음 알파벳으로 이동
    13 ~ 25까지는 이전 알파벳으로 이동

    커서를 왼쪽으로 움직일 수 있다.
    오른쪽으로도 가능하다.
    20개의 글자다.
    """
    alpha = dict(map(lambda x: (x[1], x[0]),
                 enumerate(string.ascii_uppercase)))
    move_cost = 1e10
    change_cost = 0
    # 변경하기 위한 최소 값
    for n in name:
        result = alpha[n]
        if result <= 12:
            change_cost += result
        else:
            change_cost += 25 - result + 1

    def find_min_ans(_li, return_point, cost_return):
        num_A = 0
        # return_point + 1 부터 A인 친구의 개수를 뺀다. (여기는 안 볼테니깐)
        for n in _li[return_point + 1:]:
            if n != "A":
                break
            num_A += 1

        # 변경하는데 들은 비용 + return_point까지 왔다가 돌아오는 비용 - (끝에서 return_point까지 오는 비용) - "A"의 개수
        return min(move_cost, cost_return + (len(name) - return_point - 1) - num_A)

    # 움직여야 할 최소 값을 찾아보자.
    # 길이가 20까지밖에 안된다. 완탐으로 비교
    for return_point in range(len(name)):
        # return_point까지 왔다갔다 하는 비용
        cost_return = return_point * 2
        # 정방향으로 먼저 가고 역방향으로 갔을 때의 비용
        move_cost = find_min_ans(name, return_point, cost_return)
        # 역방향으로 먼저 가고 정방향으로 갔을 때의 비용
        # 역방향으로 먼저 갔으니 + 1을 한다.
        cost_return += 1
        reverse_name = name[::-1]
        move_cost = find_min_ans(reverse_name, return_point, cost_return)

    return move_cost + change_cost
